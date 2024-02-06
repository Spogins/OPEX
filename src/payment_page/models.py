# -*- coding: utf-8 -*-
from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from components.three_tab_block.three_tab_block import ThreeTabBlock
from components.units_block.units_block import UnitsBlock
from components.video_image_chooser_block.video_image_chooser_block import VideoImageChooserBlock


class PaymentPage(Page):
    subtitle = models.CharField(max_length=255)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    video = models.ForeignKey("wagtailvideos.Video", related_name="+", null=True, blank=True, on_delete=models.SET_NULL)
    body = StreamField(
        [
            ("tab_block", ThreeTabBlock()),
            ("units_block", UnitsBlock()),
            ("video_image_chooser_block", VideoImageChooserBlock()),
        ],
        use_json_field=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("image"),
        FieldPanel("video"),
        FieldPanel("body"),
    ]
    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ]
