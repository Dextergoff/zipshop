# Generated by Django 4.1.4 on 2023-01-03 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0030_remove_item_total"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="samebilling",
            field=models.BooleanField(default=False),
        ),
    ]