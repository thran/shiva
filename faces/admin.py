from django.contrib import admin
from faces.models import Face


class FacesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Face, FacesAdmin)
