from django.contrib import admin
from faces.models import Face


class FacesAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "alternatives", "hint", "active")

admin.site.register(Face, FacesAdmin)
