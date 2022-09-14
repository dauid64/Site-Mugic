from django.contrib import admin
from .models import Projeto

class ProjectAdmin(admin.ModelAdmin):
    ...

admin.site.register(Projeto, ProjectAdmin)
