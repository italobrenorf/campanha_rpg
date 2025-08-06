from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    path('personagem/', include('Personagem.urls')),
    path('guilda/', include('Guilda.urls')),
    path('npc/', include('NPC.urls')),
    path('item/', include('Item.urls')),
    path('monstro/', include('Monstro.urls')),
    path('dungeon/', include('Dungeon.urls')),
    path('efeito/', include('Efeitos.urls')),
    path('evento/', include('Eventos.urls')),
    path('inventario/', include('Inventario.urls')),
    path('missao/', include('Missoes.urls')),
    path('usuario/', include('Usuario.urls')),
]
