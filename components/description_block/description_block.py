from wagtail.blocks import CharBlock, ListBlock, RichTextBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock


class DescriptionBlock(StructBlock):
    title = RichTextBlock()
    description = RichTextBlock()
