from django.contrib import admin

from .models import Item, ItemType, Section, Format, State, Level, Language


# Register your models here.
admin.site.register(Item)
admin.site.register(ItemType)
admin.site.register(Section)
admin.site.register(Format)
admin.site.register(State)
admin.site.register(Level)
admin.site.register(Language)
