from django.contrib import admin
from .models import WishlistItem

@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'status', 'data_adicao')
    list_filter = ('status', 'data_adicao')
    search_fields = ('nome', 'descricao', 'loja')
