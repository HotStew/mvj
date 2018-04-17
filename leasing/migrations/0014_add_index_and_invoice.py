# Generated by Django 2.0.4 on 2018-04-16 12:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import leasing.enums


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0013_add_basis_of_rent'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankHoliday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(db_index=True, unique=True, verbose_name='Day')),
            ],
            options={
                'verbose_name': 'Bank holiday',
                'verbose_name_plural': 'Bank holidays',
                'ordering': ('day',),
            },
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='Number')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Year')),
                ('month', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Month', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Index',
                'verbose_name_plural': 'Indexes',
                'ordering': ('year', 'month'),
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Time modified')),
                ('sent_to_sap_at', models.DateTimeField(blank=True, null=True, verbose_name='Sent to SAP at')),
                ('sap_id', models.CharField(blank=True, max_length=255, verbose_name='SAP ID')),
                ('due_date', models.DateField(verbose_name='Due date')),
                ('invoicing_date', models.DateField(blank=True, null=True, verbose_name='Invoicing date')),
                ('status', enumfields.fields.EnumField(enum=leasing.enums.InvoiceStatus, max_length=10, verbose_name='Status')),
                ('billing_period_start_date', models.DateField(verbose_name='Billing period start date')),
                ('billing_period_end_date', models.DateField(verbose_name='Billing period end date')),
                ('postpone_date', models.DateField(blank=True, null=True, verbose_name='Postpone date')),
                ('rent_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Rent amount')),
                ('share_numerator', models.PositiveIntegerField(verbose_name='Share numerator')),
                ('share_denominator', models.PositiveIntegerField(verbose_name='Share denominator')),
                ('billed_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Billed amount')),
                ('paid_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Paid amount')),
                ('paid_date', models.DateField(blank=True, null=True, verbose_name='Paid date')),
                ('outstanding_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Outstanding amount')),
                ('payment_notification_date', models.DateField(blank=True, null=True, verbose_name='Payment notification date')),
                ('collection_charge', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Collection charge')),
                ('payment_notification_catalog_date', models.DateField(blank=True, null=True, verbose_name='Payment notification catalog date')),
                ('delivery_method', enumfields.fields.EnumField(blank=True, enum=leasing.enums.InvoiceDeliveryMethod, max_length=10, null=True, verbose_name='Delivery method')),
                ('type', enumfields.fields.EnumField(enum=leasing.enums.InvoiceType, max_length=10, verbose_name='Type')),
                ('notes', models.TextField(blank=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
            },
        ),
        migrations.CreateModel(
            name='ReceivableType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('sap_code', models.CharField(max_length=255, verbose_name='SAP code')),
            ],
            options={
                'verbose_name': 'Receivable type',
                'verbose_name_plural': 'Receivable types',
            },
        ),
        migrations.RemoveField(
            model_name='rent',
            name='is_active',
        ),
        migrations.AddField(
            model_name='lease',
            name='is_invoicing_enabled',
            field=models.BooleanField(default=False, verbose_name='Invoicing enabled?'),
        ),
        migrations.AddField(
            model_name='lease',
            name='is_rent_info_complete',
            field=models.BooleanField(default=False, verbose_name='Rent info complete?'),
        ),
        migrations.AddField(
            model_name='rent',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End date'),
        ),
        migrations.AddField(
            model_name='rent',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start date'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='lease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoices', to='leasing.Lease', verbose_name='Lease'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='receivable_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='leasing.ReceivableType', verbose_name='Receivable type'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='leasing.Contact', verbose_name='Recipient'),
        ),
        migrations.AddIndex(
            model_name='index',
            index=models.Index(fields=['year', 'month'], name='leasing_ind_year_ffd71e_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='index',
            unique_together={('year', 'month')},
        ),
    ]
