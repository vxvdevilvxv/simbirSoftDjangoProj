from django.contrib import admin
from .models import Note

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at')
    list_display_links = ('content',)
    search_fields = ['content', 'created_at']

admin.site.register(Note, NoteAdmin)
