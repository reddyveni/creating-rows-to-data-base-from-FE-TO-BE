"""
URL configuration for proj25 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_Topic/',insert_Topic,name='insert_Topic'),
    path('insert_webpage/',insert_Webpage,name='insert_webpage'),
    path('insert_acessrecords/',insert_accessrecords,name='insert_accessrecords'),
    path('insert_topic/',retrieve_topic,name='retrieve_topic'),
    path('insert_webpage/',retrieve_Webpage,name='retrieve_webpage'),
    path('insert_accessrecords/',retrieve_accessrecords,name='retrieve_accessrecords')
]
