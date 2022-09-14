from django.urls import path
from . import views

app_name = "projetos"

urlpatterns = [
    path('', views.portfolio, name="home"),
    path('project/<int:id>', views.projeto, name="projeto")
]
