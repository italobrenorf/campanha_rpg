from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    path('jogador/', include('Jogador.urls')),
    path('guilda/', include('Guilda.urls')),
     path('npc/', include('NPC.urls')),
     path('item/', include('Item.urls')),
]
