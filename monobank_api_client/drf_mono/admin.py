from django.contrib import admin
from .models import Mono


@admin.register(Mono)
class MonoAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "mono_token",
        "date_joined",
    )
