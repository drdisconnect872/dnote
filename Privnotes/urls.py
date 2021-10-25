"""Privnotes URL Configuration

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
from django.urls import path
import notes.views as n_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',n_views.index,name='home'),
    path('view/<hash_key>', n_views.view_message, name='view_message'),
    path('hidden/<hash_key>', n_views.hidden_message, name='hidden_message'),
#    path('unhide/<hash>', n_views.unhide_message, name='unhide_message'),
#    path('viewed/<hash>', n_views.viewed_message, name='viewed_message'),
]
