# Generated by Django 4.1.3 on 2022-11-30 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("feed", "0003_post_in_carts"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="in_carts",
        ),
    ]