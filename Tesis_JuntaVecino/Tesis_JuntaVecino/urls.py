"""
URL configuration for Tesis_JuntaVecino project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Tesis_JuntaVecino import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('actas/', include('apps.actas.urls')),
    path('asistencia/', include('apps.asistencia.urls')),
    path('recursos/', include('apps.recursos.urls')),
    path('votaciones/', include('apps.votaciones.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    path('administracion/', include('apps.administracion.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('recomendaciones/', include('apps.recomendaciones.urls')),
   
]
