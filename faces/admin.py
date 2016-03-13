from django.contrib import admin
from faces.models import Face, Guess, Chat


class FacesAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "alternatives", "hint", "active")


class GuessAdmin(admin.ModelAdmin):
    list_display = ("face", "text", "who", "correct")


class ChatAdmin(admin.ModelAdmin):
    list_display = ("who", "text", "time")

admin.site.register(Face, FacesAdmin)
admin.site.register(Guess, GuessAdmin)
admin.site.register(Chat, ChatAdmin)
