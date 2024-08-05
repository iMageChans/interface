from django.contrib import admin
from main_mining.models import *


@admin.register(TotalBurned)
class TotalBurnedAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'totals', )
