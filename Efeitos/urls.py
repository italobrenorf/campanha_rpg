from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index-efeito'),
path('<int:id_efeito>/', views.detalha, name='detalhe-efeito'),
path('add/', views.cria, name='add-efeito'),
path('edit/<int:id_efeito>/', views.edita, name='edit-efeito'),
path('delete/<int:id_efeito>/', views.deleta, name='delete-efeito'),
]