# -*- coding: utf-8 -*-
import json
import re
from functools import lru_cache

from django import template

from config import settings

register = template.Library()


@lru_cache()
@register.simple_tag
def get_static_path(key):
    """
    Custom tag for getting css path with hash from manifest.json file
    """
    with open(settings.DJANGO_VITE_MANIFEST_PATH, "r") as file:
        tmp_file = json.load(file)
    value = tmp_file.get(key)
    if value:
        path_with_hash = value.get("file")
    else:
        path_with_hash = key
    return "/static/nodejs/" + path_with_hash


@register.filter(name="split")
def split(value, key):
    """
    Returns the value turned into a list.
    """
    print(value.split(key))

    return value.split(key)


@register.filter(name="split_half")
def split_half(value, key):
    """
    Returns the two part of string
    """
    original_list = value.split(key)
    middle_index = len(original_list) // 2
    first_part = " ".join(original_list[:middle_index])
    second_part = " ".join(original_list[middle_index:])

    return first_part, second_part


# tag for convert youtube url with embed
@register.simple_tag(takes_context=True)
def youtube_embed(context, youtube_url):
    print(youtube_url)
    if "embed" not in youtube_url:
        if "shorts" not in youtube_url:
            get_video_id = re.search(r"v=([^&]+)", youtube_url)
        else:
            get_video_id = re.search(r"/shorts/([A-Za-z0-9_-]+)", youtube_url)
        print(get_video_id)
        video_id = get_video_id.group(1)
        embed_url = f"https://www.youtube.com/embed/{video_id}"
        return embed_url

    return youtube_url
