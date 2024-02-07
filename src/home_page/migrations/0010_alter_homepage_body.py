# -*- coding: utf-8 -*-
# Generated by Django 4.2.9 on 2024-02-07 08:31

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations

import components.benefits_block.benefits_block
import src.wagtailvideos.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("home_page", "0009_alter_homepage_body"),
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
                                ("subtitle", wagtail.blocks.CharBlock(max_length=200, required=False)),
                                ("description", wagtail.blocks.RichTextBlock()),
                                ("gallery", wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())),
                            ],
                        ),
                    ),
                    (
                        "video_image_chooser_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                ("video", src.wagtailvideos.blocks.VideoChooserBlock(required=False)),
                                ("title", wagtail.blocks.CharBlock(max_length=200)),
                                ("subtitle", wagtail.blocks.CharBlock(max_length=200)),
                            ],
                        ),
                    ),
                    (
                        "benefits_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("subtitle", wagtail.blocks.CharBlock(required=False)),
                                (
                                    "benefits",
                                    wagtail.blocks.ListBlock(
                                        components.benefits_block.benefits_block.BenefitBlock,
                                        max_num=3,
                                        min_num=0,
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
                use_json_field=True,
            ),
        ),
    ]
