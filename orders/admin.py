from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # 显示在列表页面中的字段
    list_display = ('order_id', 'operation', 'from_address', 'to_address', 'status', 'fee', 'created_at', 'updated_at')

    # 设置可以点击进入详情页的字段（即 `order_id`）
    list_display_links = ('order_id',)

    # 添加搜索功能，可以通过 `order_id`, `from_address` 和 `to_address` 搜索
    search_fields = ('order_id', 'from_address', 'to_address', 'operation')

    # 在列表页面右侧添加过滤器
    list_filter = ('status', 'created_at', 'updated_at')

    # 只读字段，防止误操作修改这些字段
    readonly_fields = ('created_at', 'updated_at', 'transaction_result', 'error_message')

    # 细节页面中显示字段的顺序和分组
    fieldsets = (
        (None, {
            'fields': ('order_id', 'operation', 'from_address', 'to_address', 'params', 'fee', 'status')
        }),
        ('Result Information', {
            'fields': ('transaction_result', 'error_message'),
            'classes': ('collapse',),  # 这个部分可以默认收起
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )
