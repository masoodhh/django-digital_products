from django.contrib import admin

from django.contrib import admin
from .models import Product, Category, File
from import_export.admin import ImportExportModelAdmin


class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ('id','title', 'is_enabled', 'file', 'file_type')
    extra = 0


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'title', 'is_enabled', 'created_time')
    search_fields = ['title']
    list_filter = ['is_enabled']
    inlines = [FileInlineAdmin]
    filter_horizontal = ['categories']


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','title', 'is_enabled', 'created_time', 'parent')
    search_fields = ['title']
    list_filter = ('is_enabled', 'parent')
