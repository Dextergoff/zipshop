# Generated by Django 4.1.4 on 2023-01-20 21:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("center_user", "0003_user_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="user",
            name="updated",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
