# Generated by Django 4.1.3 on 2022-11-25 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("image", models.ImageField(upload_to="")),
                ("title", models.CharField(max_length=40)),
                ("price", models.FloatField()),
                ("desc", models.CharField(max_length=200)),
            ],
        ),
    ]
