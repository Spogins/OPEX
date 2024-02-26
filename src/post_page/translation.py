# -*- coding: utf-8 -*-
from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from src.post_page.models import PostPage
from src.privacy_policy_page.models import PrivacyPolicyPage


@register(PostPage)
class PostPageTranslation(TranslationOptions):
    fields = ("description",)
