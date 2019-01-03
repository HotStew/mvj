import datetime
import glob
import os
import sys
import tempfile
from decimal import Decimal
from pathlib import Path

import paramiko
import pysftp
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from paramiko import SSHException
from paramiko.py3compat import decodebytes

from laske_export.models import LaskePaymentsLog
from leasing.models import Invoice
from leasing.models.invoice import InvoicePayment


def get_import_dir():
    return os.path.join(settings.LASKE_EXPORT_ROOT, 'payments')


class Command(BaseCommand):
    help = 'Get payments from Laske'

    def download_payments(self):
        # # Add destination server host key
        if settings.LASKE_SERVERS['payments']['key_type'] == 'ssh-ed25519':
            key = paramiko.ed25519key.Ed25519Key(data=decodebytes(settings.LASKE_SERVERS['payments']['key']))
        elif 'ecdsa' in settings.LASKE_SERVERS['payments']['key_type']:
            key = paramiko.ecdsakey.ECDSAKey(data=decodebytes(settings.LASKE_SERVERS['payments']['key']))
        else:
            key = paramiko.rsakey.RSAKey(data=decodebytes(settings.LASKE_SERVERS['payments']['key']))

        hostkeys = paramiko.hostkeys.HostKeys()
        hostkeys.add(settings.LASKE_SERVERS['payments']['host'], settings.LASKE_SERVERS['payments']['key_type'], key)

        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = hostkeys
        # Or Disable key check:
        # cnopts.hostkeys = None

        with pysftp.Connection(settings.LASKE_SERVERS['payments']['host'],
                               port=settings.LASKE_SERVERS['payments']['port'],
                               username=settings.LASKE_SERVERS['payments']['username'],
                               password=settings.LASKE_SERVERS['payments']['password'],
                               cnopts=cnopts) as sftp:
            sftp.get_d(settings.LASKE_SERVERS['payments']['directory'], get_import_dir(), preserve_mtime=True)

    def check_import_directory(self):
        if not os.path.isdir(get_import_dir()):
            self.stdout.write('Directory "{}" does not exist. Please create it.'.format(get_import_dir()))
            sys.exit(-1)

        try:
            fp = tempfile.TemporaryFile(dir=get_import_dir())
            fp.close()
        except PermissionError:
            self.stdout.write('Can not create file in directory "{}".'.format(get_import_dir()))
            sys.exit(-1)

    def find_unimported_files(self):
        all_files = glob.glob(get_import_dir() + '/MR_OUT_{}_*'.format(settings.LASKE_VALUES['sender_id']))
        already_imported_filenames = LaskePaymentsLog.objects.filter(is_finished=True).values_list(
            'filename', flat=True)

        return [filename for filename in all_files if Path(filename).name not in already_imported_filenames]

    def get_payment_lines_from_file(self, filename):
        result = []

        with open(filename, 'rt') as fp:
            lines = fp.readlines()

        for line in lines:
            line = line.strip('\n')
            if len(line) != 90:
                continue
            if line[0] not in ['3', '5', '7']:
                continue

            result.append(line)

        return result

    def handle(self, *args, **options):
        self.check_import_directory()

        self.stdout.write('Connecting to the Laske payments server and downloading files...')
        try:
            self.download_payments()
            self.stdout.write('Done.')
        except SSHException as e:
            self.stdout.write('Error with the Laske payments server: {}'.format(e))

        self.stdout.write('Finding files...')
        filenames = self.find_unimported_files()
        if not filenames:
            self.stdout.write('No new files found. Exiting.')
            return

        self.stdout.write('{} new file(s) found.'.format(len(filenames)))

        self.stdout.write('Reading files...')

        for filename in filenames:
            filepath = Path(filename)

            self.stdout.write('Filename: {}'.format(filename))
            (laske_payments_log_entry, created) = LaskePaymentsLog.objects.get_or_create(
                filename=filepath.name,
                defaults={
                    "started_at": timezone.now()
                })

            lines = self.get_payment_lines_from_file(filename)

            for line in lines:
                invoice_number = int(line[43:63])
                amount = Decimal('{}.{}'.format(line[77:85], line[85:87]))
                payment_date = datetime.date(year=2000 + int(line[21:23]), month=int(line[23:25]), day=int(line[25:27]))
                filing_code = line[27:43].strip()

                self.stdout.write(' Invoice #{} amount: {} date: {} filing code: {}'.format(
                    invoice_number, amount, payment_date, filing_code))

                try:
                    invoice = Invoice.objects.get(number=invoice_number)

                    if invoice.payments.filter(filing_code=filing_code).exists():
                        self.stdout.write('  Payment already exists! Skipping.'.format(invoice_number))
                    else:
                        invoice_payment = InvoicePayment.objects.create(
                            invoice=invoice,
                            paid_amount=amount,
                            paid_date=payment_date,
                            filing_code=filing_code
                        )
                        laske_payments_log_entry.payments.add(invoice_payment)
                        invoice.update_amounts()

                except Invoice.DoesNotExist:
                    self.stdout.write('  Invoice number "{}" does not exist! Skipping.'.format(invoice_number))

            laske_payments_log_entry.ended_at = timezone.now()
            laske_payments_log_entry.is_finished = True
            laske_payments_log_entry.save()

        self.stdout.write('Done.')