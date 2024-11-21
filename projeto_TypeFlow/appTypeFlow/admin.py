from django.contrib import admin
from .models import Question, MBTIDescription, MBTIResult

# Registrar o modelo 'Question'
admin.site.register(Question)
admin.site.register(MBTIResult)

# Registrar o modelo 'MBTIDescription' com uma classe personalizada
@admin.register(MBTIDescription)
class MBTIDescriptionAdmin(admin.ModelAdmin):
    list_display = ('type', 'descrição_geral', 'sala_de_aula','grupos_de_projetos','primary_color', 'background_color')
    search_fields = ('type',)