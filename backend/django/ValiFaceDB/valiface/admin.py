from django.contrib import admin
import valiface.models

# Register your models here.

admin.site.register(valiface.models.Gerente)
admin.site.register(valiface.models.Funcionario)
admin.site.register(valiface.models.Ambiente)
admin.site.register(valiface.models.Acesso)