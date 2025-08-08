from django.contrib import admin

from .models import Flower

class FlowerAdmin(admin.ModelAdmin):
    list_display = ['id', 'sort', 'price', 'color', 'stock']

admin.site.register(Flower, FlowerAdmin)


