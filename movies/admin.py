from django.contrib import admin
from .models import Gore
# Register your models here.

@admin.register(Gore)
class GoreAdmin(admin.ModelAdmin):
    pass