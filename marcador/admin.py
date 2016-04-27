from django.contrib import admin
from .models import Bookmark, Tag

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'owner', 'is_public', 'date_update')
    list_editable = ('is_public',)
    list_filter = ('is_public', 'owner__username')
    search_fields = ['url', 'title', 'description']
    readonly_fields = ('date_created', 'date_update')


admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag)