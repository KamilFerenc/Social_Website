from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'created')


admin.site.register(Image, ImageAdmin)