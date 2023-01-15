# Generated by Django 4.1.3 on 2022-12-15 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cart", "0005_cartitem_total"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=999)),
                ("street_adress", models.CharField(max_length=999)),
                ("apartment", models.CharField(max_length=999)),
                ("country", models.CharField(max_length=999)),
                ("state", models.CharField(max_length=999)),
                ("zip_code", models.IntegerField()),
                ("is_billing", models.BooleanField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Cart",
        ),
    ]