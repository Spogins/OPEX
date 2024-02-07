# -*- coding: utf-8 -*-
# Generated by Django 4.2.9 on 2024-02-07 08:33

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models

import src.wagtailvideos.blocks


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("wagtailvideos", "0002_alter_video_thumbnail"),
        ("wagtailcore", "0090_page_search_description_en_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="GalleryPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("subtitle", models.CharField(max_length=255)),
                ("subtitle_uk", models.CharField(max_length=255, null=True)),
                ("subtitle_en", models.CharField(max_length=255, null=True)),
                ("subtitle_ru", models.CharField(max_length=255, null=True)),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "gallery",
                                wagtail.blocks.ListBlock(
                                    wagtail.blocks.StructBlock(
                                        [
                                            ("image", wagtail.images.blocks.ImageChooserBlock()),
                                            ("video", src.wagtailvideos.blocks.VideoChooserBlock(required=False)),
                                            ("title", wagtail.blocks.CharBlock(max_length=200)),
                                            ("subtitle", wagtail.blocks.CharBlock(max_length=200)),
                                        ],
                                    ),
                                ),
                            ),
                        ],
                        use_json_field=True,
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "video",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailvideos.video",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
