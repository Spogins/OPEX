# -*- coding: utf-8 -*-
from wagtail.blocks import CharBlock, IntegerBlock, StreamBlock, StructBlock


class UnitItem(StructBlock):
    value = IntegerBlock()
    measure_unit = CharBlock()
    title = CharBlock()


class UnitsBlock(StreamBlock):
    unit_item = UnitItem()

    class Meta:
        template = ("units_block/units_block.html",)
        max_num = 4
