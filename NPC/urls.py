from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index-npc'),
path('<int:id_npc>/', views.detalha, name='detalhe-npc'),
path('add/', views.cria, name='add-npc'),
path('edit/<int:id_npc>/', views.edita, name='edit-npc'),
path('delete/<int:id_npc>/', views.deleta, name='delete-npc'),
]