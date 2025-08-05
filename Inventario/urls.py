from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index-inventario'),
path('<int:id_inventario>/', views.detalha, name='detalhe-inventario'),
path('add/', views.cria, name='add-inventario'),
path('edit/<int:id_inventario>/', views.edita, name='edit-inventario'),
path('delete/<int:id_inventario>/', views.deleta, name='delete-inventario'),
]