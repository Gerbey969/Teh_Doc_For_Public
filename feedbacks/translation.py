from django.conf import settings
from django.utils.translation import ugettext_lazy
from .models import Category
from modeltranslation.translator import translator, TranslationOptions


class CategoryTransaltionOption(TranslationOptions):
    fields = ('name', )


translator.register(Category, CategoryTransaltionOption)