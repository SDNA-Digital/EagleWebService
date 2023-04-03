"""raspagem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from rasp.views import current_datetime, HelloWorld
from rasp.viewsInportWord import InportWord
from rasp.viewsExcel import InportExcel
from rasp.viewspdf import Inportpdf
from rasp.viewsNatureza import import_natureza_atividade

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloWorld),
    path('script/', current_datetime),
    path('import/natureza-atividade/', import_natureza_atividade),
    path('inportword/<path:caminho>/<slug:id>/<slug:tabela>/<slug:campo>/<slug:indice>/', InportWord),
    path('inportexcel/<slug:id>/', InportExcel),
    path('inportpdf/<path:caminho>/<slug:id>/<slug:tabela>/<slug:campo>/<slug:indice>/', Inportpdf),
]
