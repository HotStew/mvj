# Generated by Django 3.2.9 on 2021-11-02 11:58

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("credit_integration", "0007_add_verbose"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creditdecision",
            name="original_data",
            field=models.JSONField(
                blank=True,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                null=True,
                verbose_name="original_data",
            ),
        ),
    ]