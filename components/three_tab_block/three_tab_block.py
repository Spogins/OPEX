# -*- coding: utf-8 -*-
from wagtail.blocks import CharBlock, ListBlock, RichTextBlock, StreamBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock


class ItemDescription(StructBlock):
    title = CharBlock()
    description = RichTextBlock()
    icon = ImageChooserBlock()


class TabBlock(StructBlock):
    title = CharBlock()
    subtitle = CharBlock()
    image = ImageChooserBlock()
    tab_item_description = ListBlock(ItemDescription(), max_num=3)


class ThreeTabBlock(StreamBlock):
    tab = TabBlock()

    class Meta:
        template = ("three_tab_block/three_tab_block.html",)
        max_num = 3
