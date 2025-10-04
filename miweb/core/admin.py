from django.contrib import admin
from .models import cotizador

@admin.register(cotizador)
class cotizadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'mensaje', 'fecha')  
    search_fields = ('nombre', 'email')
