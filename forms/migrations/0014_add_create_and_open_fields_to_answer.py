# Generated by Django 3.2.12 on 2022-02-23 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0013_alter_attachment_attachment"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="answer",
            name="opened_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
