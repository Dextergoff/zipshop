# Generated by Django 4.1.3 on 2022-11-26 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0002_rename_cartmodel_cart"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="cart_total",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
