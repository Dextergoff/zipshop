# Generated by Django 4.1.4 on 2022-12-21 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0007_rename_is_billing_address_def_address"),
    ]

    operations = [
        migrations.RenameField(
            model_name="address",
            old_name="street_adress",
            new_name="street_address",
        ),
    ]