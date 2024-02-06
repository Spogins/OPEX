# -*- coding: utf-8 -*-
from wagtail.blocks import CharBlock, ListBlock, RichTextBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock


class TextWithGalleryBlock(StructBlock):
    title = CharBlock(max_length=200)
    subtitle = CharBlock(max_length=200, required=False)
    description = RichTextBlock()
    gallery = ListBlock(ImageChooserBlock())

    class Meta:
        template = "text_with_gallery_block/text_with_gallery_block.html"
