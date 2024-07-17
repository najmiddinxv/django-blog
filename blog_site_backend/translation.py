from modeltranslation.translator import translator, TranslationOptions
from .models import Tag, Categories

class TagTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Tag, TagTranslationOptions)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Categories, CategoriesTranslationOptions)
