from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index-evento'),
path('<int:id_evento>/', views.detalha, name='detalhe-evento'),
path('add/', views.cria, name='add-evento'),
path('edit/<int:id_evento>/', views.edita, name='edit-evento'),
path('delete/<int:id_evento>/', views.deleta, name='delete-evento'),
]