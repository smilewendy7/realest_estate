from django.contrib import admin

# Register your models here.
from .models import Vender

# Register your models here.

class VenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'date_joined')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Vender, VenderAdmin)