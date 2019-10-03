from django.core.management.base import BaseCommand

from leasing.importer.area import AreaImporter
from leasing.importer.basis_of_rent import BasisOfRentImporter
from leasing.importer.invoice_relations import InvoiceRelationsImporter
from leasing.importer.lease import LeaseImporter
from leasing.importer.lease_area import LeaseAreaImporter
from leasing.importer.lease_relations import LeaseRelationsImporter


class Command(BaseCommand):
    help = 'Import data'

    def __init__(self, stdout=None, stderr=None, no_color=False):
        super().__init__(stdout=stdout, stderr=stderr, no_color=no_color)

        self.importers = [
            BasisOfRentImporter,
            LeaseImporter,
            LeaseRelationsImporter,
            AreaImporter,
            LeaseAreaImporter,
            InvoiceRelationsImporter,
        ]

        self._importers = {}
        for importer in self.importers:
            self._importers[importer.type_name] = importer

    def add_arguments(self, parser):
        importer_choices = self._importers.keys()

        parser.add_argument('types', nargs='+', type=str, choices=importer_choices, help='types of data to import')

        for importer in self.importers:
            importer.add_arguments(parser)

    def handle(self, *args, **options):
        for importer_type_name in options['types']:
            importer = self._importers[importer_type_name](stdout=self.stdout, stderr=self.stderr)
            importer.read_options(options)
            importer.execute()
