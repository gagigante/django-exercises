"""g4car URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from core.views import home, cadastro_cliente, listagem_clientes, \
                cadastro_veiculo, listagem_veiculos, Registrar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='url_principal'),
    path('registrar/', Registrar.as_view(), name='url_registrar'),
    path('cadastro_cliente/', cadastro_cliente, name='url_cadastro_cliente'),
    path('listagem_clientes/', listagem_clientes, name='url_listagem_clientes'),
    path('cadastro_veiculo/', cadastro_veiculo, name='url_cadastro_veiculo'),
    path('listagem_veiculos/', listagem_veiculos, name='url_listagem_veiculos'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)