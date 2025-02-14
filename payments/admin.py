from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Gateway, Payment


@admin.register(Gateway)
class GatewayAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['title', 'is_enable']


@admin.register(Payment)
class PaymentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['user', 'package', 'gateway', 'price', 'status', 'phone_number', 'created_time']
    list_filter = ['status', 'gateway', 'package']
    search_fields = ['user__username', 'phone_number']