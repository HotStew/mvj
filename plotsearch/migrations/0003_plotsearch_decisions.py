# Generated by Django 2.2.24 on 2021-09-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leasing", "0045_move_plotsearch_to_plotsearch_app"),
        ("plotsearch", "0002_plotsearch_form"),
    ]

    operations = [
        migrations.AddField(
            model_name="plotsearch",
            name="decisions",
            field=models.ManyToManyField(
                blank=True, related_name="plot_searches", to="leasing.Decision"
            ),
        ),
    ]
