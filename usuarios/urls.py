from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('validar_cadastro/', views.valida_cadastro, name='valida_cadastro'),
    path('validar_login/', views.valida_login, name='valida_login'),
    path('sair/', views.sair, name='sair'),


]