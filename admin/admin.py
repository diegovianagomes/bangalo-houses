from django.contrib import admin
from .models import Supplier, Architect, House, HouseImages 

class HouseImageInline(admin.TabularInline):
    model = HouseImages
    extra = 1

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'country', 'email', 'created_at')
    search_fields = ('company_name', 'country')

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'country', 'supplier', 'is_active')
    list_filter = ('country', 'is_active', 'supplier')
    search_fields = ('title', 'description', 'architect')
    inlines = [HouseImageInline]
