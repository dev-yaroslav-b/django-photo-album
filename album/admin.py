from django.contrib import admin
from .models import MediaPost


class MediaPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'description', 'media', 'created_date')


admin.site.register(MediaPost, MediaPostAdmin)
