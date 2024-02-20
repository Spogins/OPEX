# -*- coding: utf-8 -*-
from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from src.privacy_policy_page.models import PrivacyPolicyPage


@register(PrivacyPolicyPage)
class PrivacyPolicyPageTranslation(TranslationOptions):
    fields = ("description",)
