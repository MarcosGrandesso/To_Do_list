from django.contrib import admin

from .models import Tarefas, Prioridade
# Register your models here.

admin.site.register(Tarefas)
admin.site.register(Prioridade)