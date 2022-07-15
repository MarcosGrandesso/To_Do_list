"""To_Do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from To_Do_list.views import index, login, new_task, register

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('new-task/',new_task, name='taskn'),
    path('register/',register, name='register'),
    path('/contas/login/', login, name='login') ,
    path('contas/', include('django.contrib.auth.urls')),
]
