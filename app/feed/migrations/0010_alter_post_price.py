# Generated by Django 4.1.4 on 2023-01-13 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feed", "0009_hashtag_post_hashtags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=99),
        ),
    ]