# -*- coding: utf-8 -*-
# Generated by Django 4.2.9 on 2024-02-06 09:38

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home_page", "0003_alter_homepage_image_alter_homepage_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "units_block",
                        wagtail.blocks.StreamBlock(
                            [
                                (
                                    "unit_item",
                                    wagtail.blocks.StructBlock(
                                        [
                                            ("value", wagtail.blocks.IntegerBlock()),
                                            ("measure_unit", wagtail.blocks.CharBlock()),
                                            ("title", wagtail.blocks.CharBlock()),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ),
                    (
                        "text_with_gallery_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(max_length=200)),
                                ("subtitle", wagtail.blocks.CharBlock(max_length=200)),
                                ("description", wagtail.blocks.RichTextBlock()),
                                ("gallery", wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())),
                            ],
                        ),
                    ),
                ],
                use_json_field=True,
            ),
        ),
    ]
