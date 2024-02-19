# -*- coding: utf-8 -*-
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class SeoCustomPanel:
    seo_meta_panels = [
        MultiFieldPanel(
            [
                FieldPanel("slug"),
                FieldPanel("seo_title"),
                FieldPanel("search_description"),
                FieldPanel(
                    "canonical_url",
                    heading="Каноническая ссылка",
                    help_text="Оставьте поле пустым, чтобы использовать URL-адрес страницы.",
                ),
                FieldPanel(
                    "og_image",
                    heading="Изображение для предпросмотра",
                    help_text="Отображается при ссылке на эту страницу в социальных сетях.",
                ),
            ],
            "Поиск и просмотр в социальных сетях",
        ),
    ]
