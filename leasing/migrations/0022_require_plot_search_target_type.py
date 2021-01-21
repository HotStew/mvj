# Generated by Django 2.2.13 on 2020-10-27 07:25

import enumfields.fields
from django.db import migrations

import leasing.enums


class Migration(migrations.Migration):

    dependencies = [
        ("leasing", "0021_reform_plot_search_types"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plotsearchtarget",
            name="target_type",
            field=enumfields.fields.EnumField(
                enum=leasing.enums.PlotSearchTargetType,
                max_length=30,
                verbose_name="Target type",
            ),
        ),
    ]