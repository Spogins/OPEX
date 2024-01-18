# -*- coding: utf-8 -*-
from wagtail.blocks import CharBlock, RichTextBlock, StreamBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock


class ItemDescription(StructBlock):
    title = CharBlock()
    description = RichTextBlock()
    icon = ImageChooserBlock()


class TabItemDescriptionBlock(StreamBlock):
    description = ItemDescription()

    class Meta:
        max_num = 3
