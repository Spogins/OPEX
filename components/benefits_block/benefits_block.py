# -*- coding: utf-8 -*-
from wagtail.blocks import CharBlock, RichTextBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock


class BenefitBlock(StructBlock):
    title = CharBlock()
    description = RichTextBlock()
    image = ImageChooserBlock()


class BenefitsBlock(StructBlock):
    title = CharBlock()
    subtitle = CharBlock(required=False)
    benefit_1 = BenefitBlock()
    benefit_2 = BenefitBlock()
    benefit_3 = BenefitBlock()

    class Meta:
        template = "benefits_block/benefits_block.html"
