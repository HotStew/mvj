# Generated by Django 3.2.9 on 2021-12-13 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plotsearch", "0008_add_ordering_field_plotsearchtype"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="plotsearchsubtype",
            options={
                "ordering": ["ordering", "name"],
                "verbose_name": "Plot search subtype",
                "verbose_name_plural": "Plot search subtypes",
            },
        ),
        migrations.AddField(
            model_name="plotsearchsubtype",
            name="ordering",
            field=models.PositiveSmallIntegerField(db_index=True, default=0),
        ),
    ]