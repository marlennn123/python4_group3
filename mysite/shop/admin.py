from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *

admin.site.register(Category)
admin.site.register(Clothes)
admin.site.register(Person)
admin.site.register(Basket)
admin.site.register(Favorite)
admin.site.register(Order)
admin.site.register(News)
admin.site.register(Color)


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ("title_product",)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

