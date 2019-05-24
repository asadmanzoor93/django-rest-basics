from django.contrib import admin

from snippets.models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'code')


admin.site.register(Snippet, SnippetAdmin)
