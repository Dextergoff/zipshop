# Generated by Django 4.1.4 on 2022-12-21 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0012_address_stateforeign"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="address",
            name="stateforeign",
        ),
        migrations.AddField(
            model_name="address",
            name="selected",
            field=models.BooleanField(default=False),
        ),
    ]
