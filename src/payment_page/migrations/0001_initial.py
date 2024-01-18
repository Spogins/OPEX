# -*- coding: utf-8 -*-
# Generated by Django 4.2.9 on 2024-01-18 11:47

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailvideos", "0002_alter_video_thumbnail"),
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("wagtailcore", "0090_page_search_description_en_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentPage",
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
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "tab_block",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "tab",
                                            wagtail.blocks.StreamBlock(
                                                [
                                                    ("title", wagtail.blocks.CharBlock()),
                                                    ("subtitle", wagtail.blocks.CharBlock()),
                                                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                                                    (
                                                        "tab_item_description",
                                                        wagtail.blocks.StructBlock(
                                                            [
                                                                ("title", wagtail.blocks.CharBlock()),
                                                                ("description", wagtail.blocks.RichTextBlock()),
                                                                ("icon", wagtail.images.blocks.ImageChooserBlock()),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                        use_json_field=True,
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "video",
                    models.ForeignKey(
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