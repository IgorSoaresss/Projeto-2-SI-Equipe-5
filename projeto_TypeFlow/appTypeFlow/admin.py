from django.contrib import admin
from .models import Question, MBTIDescription, MBTIResult, Turmas

# Registrar o modelo 'Question'
admin.site.register(Question)
admin.site.register(MBTIResult)

# Registrar o modelo 'MBTIDescription' com uma classe personalizada
@admin.register(MBTIDescription)
class MBTIDescriptionAdmin(admin.ModelAdmin):
    list_display = ('type', 'descricaoGeral', 'classe', 'subclasse', 'salaDeAula', 'gruposDeProjetos','primary_color', 'background_color', 'sidebar_color')
    search_fields = ('type',)

@admin.register(Turmas)
class turmasAdmin(admin.ModelAdmin):
    list_display = ('curso', 'periodo', 'turma')
    search_fields = ('curso',)