# Generated by Django 2.2.2 on 2019-06-12 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0071_reservationprocedure'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenantRentShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Time modified')),
                ('share_numerator', models.PositiveIntegerField(verbose_name='Rent share numerator')),
                ('share_denominator', models.PositiveIntegerField(verbose_name='Rent share denominator')),
                ('intended_use', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='leasing.RentIntendedUse', verbose_name='Intended use')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rent_shares', to='leasing.Tenant', verbose_name='Tenant')),
            ],
            options={
                'verbose_name': 'Tenant rent share',
                'verbose_name_plural': 'Tenant rent shares',
            },
        ),
    ]