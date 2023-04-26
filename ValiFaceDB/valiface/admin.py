from django.contrib import admin
import valiface.models

# Register your models here.

admin.site.register(valiface.models.Agente)
admin.site.register(valiface.models.Funcionario)
admin.site.register(valiface.models.Setor)
admin.site.register(valiface.models.Cadastro)
admin.site.register(valiface.models.Categoria)
admin.site.register(valiface.models.Licenca)