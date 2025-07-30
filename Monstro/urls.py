from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index-monstro'),
path('<int:id_monstro>/', views.detalha, name='detalhe-monstro'),
path('add/', views.cria, name='add-monstro'),
path('edit/<int:id_monstro>/', views.edita, name='edit-monstro'),
path('delete/<int:id_monstro>/', views.deleta, name='delete-monstro'),
]