# -*- coding: utf-8 -*-
from wagtail.blocks import CharBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock

from src.wagtailvideos.blocks import VideoChooserBlock


class VideoImageChooserBlock(StructBlock):
    image = ImageChooserBlock()
    video = VideoChooserBlock(required=False)
    title = CharBlock(max_length=200)
    subtitle = CharBlock(max_length=200)

    class Meta:
        template = "video_image_chooser_block/video_image_chooser_block.html"
