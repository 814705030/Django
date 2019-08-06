"""access_ms1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from login import views as l_views
from record import views as r_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('base/', views.base),
    path('', l_views.select_index),
    path('select/', l_views.select_index),
    path('index/', r_views.index),
    path('login/', l_views.login),
    path('register/', l_views.register),
    path('logout/', l_views.logout),
    path('captcha', include('captcha.urls')),
    path('user/', r_views.user),
    path('visitor/', r_views.visitor),
    path('search/',l_views.search),
]
