# -*- coding: utf-8 -*-
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import ListBlock
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtailseo.models import SeoMixin

from components.video_image_chooser_block.video_image_chooser_block import VideoImageChooserBlock
from src.base.panels import SeoCustomPanel


class GalleryPage(SeoMixin, Page):
    subtitle = models.CharField(max_length=255)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    video = models.ForeignKey("wagtailvideos.Video", related_name="+", blank=True, null=True, on_delete=models.SET_NULL)
    gallery_title = models.CharField(max_length=255)
    gallery_subtitle = models.CharField(max_length=255)
    body = StreamField(
        [
            ("gallery", ListBlock(VideoImageChooserBlock(), template="base/gallery_list.html")),
        ],
        block_counts={
            "gallery": {"min_num": 1, "max_num": 1},
        },
        use_json_field=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("image"),
        FieldPanel("video"),
        FieldPanel("gallery_title"),
        FieldPanel("gallery_subtitle"),
        FieldPanel("body"),
    ]
    promote_panels = SeoCustomPanel.seo_meta_panels
