# Generated by Django 3.2.10 on 2021-12-22 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("plotsearch", "0010_add_translations"),
    ]

    operations = [
        migrations.CreateModel(
            name="Favourite",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FavouriteTarget",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "favourite",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="targets",
                        to="plotsearch.favourite",
                    ),
                ),
                (
                    "plot_search_target",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plotsearch.plotsearchtarget",
                    ),
                ),
            ],
        ),
    ]
