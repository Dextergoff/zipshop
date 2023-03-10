# Generated by Django 4.1.4 on 2023-01-20 20:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("feed", "0013_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="favorites",
            field=models.ManyToManyField(
                blank=True, related_name="favorites", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="hashtags",
            field=models.ManyToManyField(blank=True, to="feed.hashtag"),
        ),
        migrations.AlterField(
            model_name="post",
            name="images",
            field=models.ManyToManyField(blank=True, to="feed.image"),
        ),
        migrations.AlterField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
