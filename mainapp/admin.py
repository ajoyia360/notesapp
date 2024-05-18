from django.contrib import admin
from mainapp.models import NoteModel

class NoteModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_screenshot')  # Define fields to display in the list view
    readonly_fields = ('display_screenshot',)  # Make screenshot field read-only

    def display_screenshot(self, obj):
        if obj.screen_shoot:
            return f'<img src="{obj.screen_shoot.url}" width="100" height="auto" />'
        else:
            return 'No Screenshot'
    display_screenshot.allow_tags = True
    display_screenshot.short_description = 'Screenshot'  # Set column header name

# Register the custom admin class
admin.site.register(NoteModel, NoteModelAdmin)
