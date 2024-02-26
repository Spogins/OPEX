from wagtail.blocks import CharBlock, ListBlock, RichTextBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageTextBlock(StructBlock):
    image = ImageChooserBlock()
    description = RichTextBlock()
