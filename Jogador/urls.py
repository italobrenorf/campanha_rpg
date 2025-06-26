from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index-jogador'),
path('<int:id_jogador>/', views.detalha, name='detalhe-jogador'),
path('add/', views.cria, name='add-jogador'),
path('edit/<int:id_jogador>/', views.edita, name='edit-jogador'),
path('delete/<int:id_jogador>/', views.deleta, name='delete-jogador'),
]