from django.contrib import admin
from .models import GroceryItem

@admin.register(GroceryItem)
class GroceryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'expiry_date')
    search_fields = ('name', 'category')
    list_filter = ('category', 'expiry_date')