from django.contrib import admin

from apps.properties.models import Property, PropertyViews


class PropertyAdmin(admin.ModelAdmin):
    list = ["title", "country", "advert_type", "property_type"]
    list_filter = ["advert_type", "property_type", "country"]


admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyViews)
