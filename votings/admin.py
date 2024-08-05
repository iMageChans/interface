from django.contrib import admin
from .models import Rank


class RankAdmin(admin.ModelAdmin):
    list_display = ('node_id', 'node_name', 'sharing_percent', 'accumulative_votes', 'created_at', 'updated_at')
    list_display_links = ('node_id', 'node_name')
    search_fields = ('node_id', 'node_name')
    list_filter = ('sharing_percent', 'accumulative_votes', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('node_id', 'node_name', 'sharing_percent', 'accumulative_votes')
        }),
        ('time', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


admin.site.register(Rank, RankAdmin)
