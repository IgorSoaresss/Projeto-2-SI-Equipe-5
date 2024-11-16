from django.contrib import admin
from .models import Question, MBTIDescription

# Registrar o modelo 'Question'
admin.site.register(Question)

# Registrar o modelo 'MBTIDescription' com uma classe personalizada
@admin.register(MBTIDescription)
class MBTIDescriptionAdmin(admin.ModelAdmin):
    list_display = ('type', 'description', 'primary_color', 'background_color')
    search_fields = ('type',)