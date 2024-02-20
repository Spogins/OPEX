# -*- coding: utf-8 -*-
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtailseo.models import SeoMixin

from src.base.panels import SeoCustomPanel


class PrivacyPolicyPage(SeoMixin, Page):
    description = RichTextField()
    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]
    promote_panels = SeoCustomPanel.seo_meta_panels
