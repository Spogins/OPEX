# -*- coding: utf-8 -*-

from django.utils.safestring import mark_safe
from wagtail.images.formats import Format, register_image_format, unregister_image_format


class DefaultImageFormat(Format):
    def editor_attributes(self, image, alt_text):
        # need to add contenteditable=false to prevent editing within the embed
        original_attrs = super(DefaultImageFormat, self).editor_attributes(image, alt_text)
        original_attrs["contenteditable"] = "false"
        return original_attrs

    def image_to_html(self, image, alt_text, extra_attributes=None):
        if image.filename.split(".")[-1] == "gif":
            image_rendition = image.get_rendition("format-webp")
        else:
            image_rendition = image.get_rendition("format-jpeg")

        # get name image
        image_path = image_rendition.full_url.split("/")[-1]

        image_tag = """
                    <img src="{}" alt="{}" loading="lazy" class="_img_resp">
                    """.format(
            getattr(image_rendition, "full_url", "").replace(image_rendition.full_url, f"/media/images/{image_path}"),
            # image_rendition.full_url.replace(image_rendition.full_url, image_path),
            alt_text,
        )

        return mark_safe(image_tag)


unregister_image_format("fullwidth")
unregister_image_format("left")
unregister_image_format("right")

register_image_format(DefaultImageFormat("Default", "Default image", "", "format-jpeg"))
