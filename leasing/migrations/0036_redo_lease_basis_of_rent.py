# Generated by Django 2.1.3 on 2018-11-27 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import enumfields.fields
import leasing.enums


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leasing', '0035_add_manual_ratio_to_rent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leasebasisofrent',
            name='amount_per_floor_m2_index',
        ),
        migrations.RemoveField(
            model_name='leasebasisofrent',
            name='amount_per_floor_m2_index_100',
        ),
        migrations.RemoveField(
            model_name='leasebasisofrent',
            name='floor_m2',
        ),
        migrations.RemoveField(
            model_name='leasebasisofrent',
            name='percent',
        ),
        migrations.RemoveField(
            model_name='leasebasisofrent',
            name='year_rent_index',
        ),
        migrations.RemoveField(
            model_name='leasebasisofrent',
            name='year_rent_index_100',
        ),
        migrations.AddField(
            model_name='leasebasisofrent',
            name='amount_per_area',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Amount per area (index 100)'),
        ),
        migrations.AddField(
            model_name='leasebasisofrent',
            name='area',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Area amount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leasebasisofrent',
            name='area_unit',
            field=enumfields.fields.EnumField(blank=True, enum=leasing.enums.AreaUnit, max_length=20, null=True, verbose_name='Area unit'),
        ),
        migrations.AddField(
            model_name='leasebasisofrent',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Time created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leasebasisofrent',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='leasebasisofrent',
            name='discount_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Discount percentage'),
        ),
        migrations.AddField(
            model_name='leasebasisofrent',
            name='locked_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Locked at'),
        ),
        migrations.AddField(
            model_name='leasebasisofrent',
            name='locked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='basis_of_rents_locked', to=settings.AUTH_USER_MODEL, verbose_name='Locked by'),
        ),
        migrations.AddField(
            model_name='leasebasisofrent',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Time modified'),
        ),
        migrations.AddField(
            model_name='leasebasisofrent',
            name='plans_inspected_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Plans inspected at'),
        ),
        migrations.AddField(
            model_name='leasebasisofrent',
            name='plans_inspected_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='basis_of_rents_plans_inspected', to=settings.AUTH_USER_MODEL, verbose_name='Plans inspected by'),
        ),
        migrations.AddField(
            model_name='leasebasisofrent',
            name='profit_margin_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Profit margin percentage'),
        ),
        migrations.AlterField(
            model_name='leasebasisofrent',
            name='index',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='leasing.Index', verbose_name='Index'),
        ),
    ]