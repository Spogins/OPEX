# -*- coding: utf-8 -*-
from wagtail.blocks import StreamBlock

from components.tab_block.tab_block import TabBlock


class ThreeTabBlock(StreamBlock):
    tab = TabBlock()

    class Meta:
        max_num = 3
