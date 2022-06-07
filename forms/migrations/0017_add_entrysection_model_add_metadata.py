# Generated by Django 3.2.13 on 2022-05-23 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0016_entry_path"),
    ]

    operations = [
        migrations.RemoveField(model_name="entry", name="answer",),
        migrations.AddField(
            model_name="attachment",
            name="path",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="EntrySection",
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
                ("metadata", models.JSONField(null=True)),
                ("identifier", models.SlugField()),
                (
                    "answer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="entry_sections",
                        to="forms.answer",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="entry",
            name="entry_section",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="entries",
                to="forms.entrysection",
            ),
        ),
    ]