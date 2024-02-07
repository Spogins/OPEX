# -*- coding: utf-8 -*-
# Generated by Django 4.2.9 on 2024-02-06 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("wagtailvideos", "0002_alter_video_thumbnail"),
        ("home_page", "0002_homepage_subtitle_en_homepage_subtitle_ru_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="image",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="video",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailvideos.video",
            ),
        ),
    ]