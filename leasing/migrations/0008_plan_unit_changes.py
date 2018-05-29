# Generated by Django 2.0.5 on 2018-05-25 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0007_add_invoice_row'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanUnitIntendedUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlotDivisionState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='planunit',
            name='detailed_plan_date_of_approval',
        ),
        migrations.AddField(
            model_name='planunit',
            name='detailed_plan_latest_processing_date',
            field=models.DateField(blank=True, null=True, verbose_name='Detailed plan latest processing date'),
        ),
        migrations.AddField(
            model_name='planunit',
            name='detailed_plan_latest_processing_date_note',
            field=models.TextField(blank=True, null=True, verbose_name='Note for latest processing date'),
        ),
        migrations.AddField(
            model_name='plot',
            name='repeal_date',
            field=models.DateField(blank=True, null=True, verbose_name='Repeal date'),
        ),
        migrations.AlterField(
            model_name='planunit',
            name='detailed_plan_identifier',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Detailed plan identifier'),
        ),
        migrations.AlterField(
            model_name='planunit',
            name='plan_unit_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='leasing.PlanUnitState', verbose_name='Plan unit state'),
        ),
        migrations.AlterField(
            model_name='planunit',
            name='plan_unit_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='leasing.PlanUnitType', verbose_name='Plan unit type'),
        ),
        migrations.AlterField(
            model_name='planunit',
            name='plot_division_date_of_approval',
            field=models.DateField(blank=True, null=True, verbose_name='Plot division date of approval'),
        ),
        migrations.AlterField(
            model_name='planunit',
            name='plot_division_identifier',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Plot division identifier'),
        ),
        migrations.AddField(
            model_name='planunit',
            name='plan_unit_intended_use',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='leasing.PlanUnitIntendedUse', verbose_name='Plan unit intended use'),
        ),
        migrations.AddField(
            model_name='planunit',
            name='plot_division_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='leasing.PlotDivisionState', verbose_name='Plot division state'),
        ),
    ]