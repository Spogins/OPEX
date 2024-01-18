# -*- coding: utf-8 -*-
from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from src.payment_page.models import PaymentPage


@register(PaymentPage)
class PaymentPageTranslation(TranslationOptions):
    fields = ("subtitle",)
