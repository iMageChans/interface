from django.contrib import admin
from .models import TransactionRecord


@admin.register(TransactionRecord)
class TransactionRecordAdmin(admin.ModelAdmin):
    # 显示的字段
    list_display = ('user', 'operation', 'status', 'token', 'created_at', 'updated_at')

    # 可搜索的字段
    search_fields = ('user', 'operation')

    # 筛选器
    list_filter = ('status', 'token', 'created_at')

    # 只读字段
    readonly_fields = ('created_at', 'updated_at')

    # 定制表单字段顺序
    fieldsets = (
        (None, {
            'fields': ('user', 'operation', 'params', 'status', 'token')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

