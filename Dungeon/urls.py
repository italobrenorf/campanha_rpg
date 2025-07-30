from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index-dungeon'),
path('<int:id_dungeon>/', views.detalha, name='detalhe-dungeon'),
path('add/', views.cria, name='add-dungeon'),
path('edit/<int:id_dungeon>/', views.edita, name='edit-dungeon'),
path('delete/<int:id_dungeon>/', views.deleta, name='delete-dungeon'),
]