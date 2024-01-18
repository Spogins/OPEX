# -*- coding: utf-8 -*-
from wagtail.blocks import CharBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock

from components.tab_item_description_block.tab_item_description_block import TabItemDescriptionBlock


class TabBlock(StructBlock):
    title = CharBlock()
    subtitle = CharBlock()
    image = ImageChooserBlock()
    tab_item_description = TabItemDescriptionBlock()
