from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtailseo.models import SeoMixin
from django.db import models

from components.description_block.description_block import DescriptionBlock
from components.image_text_block.image_text_block import ImageTextBlock
from src.base.panels import SeoCustomPanel


class PostPage(SeoMixin, Page):
    main_title = models.CharField()
    date = models.DateField()
    content_first = StreamField(
        [("content_first", ImageTextBlock())],
        null=True,
        use_json_field=True,
        min_num=1,
        max_num=1,
    )
    description = StreamField(
        [("description", DescriptionBlock())],
        null=True,
        use_json_field=True,
        min_num=1,
        max_num=1,
    )
    content_second = StreamField(
        [("content_second", ImageTextBlock())],
        null=True,
        use_json_field=True,
        min_num=1,
        max_num=1,
    )
    content_panels = Page.content_panels + [
        FieldPanel("main_title"),
        FieldPanel("date"),
        FieldPanel("content_first"),
        FieldPanel("description"),
        FieldPanel("content_second"),
    ]
    promote_panels = SeoCustomPanel.seo_meta_panels
