"""blog1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from blog import views

urlpatterns = [
#path('patron', vista a la que me lleva)
    path('admin/', admin.site.urls),
    path('', views.post_list),
    path('articulo/<int:id_art>', views.detail, name='post'),
    path('articulo/<int:id_art>/comentario', views.ComentarioFormView.as_view(), name='comentar'),

    # path('contacto-email', views.contacto_email, name='contacto-email'),
    path('contacto-email', views.ContactoFormView.as_view(), name='contacto-email'),

    path('exito', views.exito),
]
