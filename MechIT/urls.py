"""MechIT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from . import views
from accounts.views import signup_view, activation_sent_view, activate

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'',include('accounts.urls')),
    url(r'^$',views.HomePage.as_view(),name='home'),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    url(r'^signup/$', signup_view, name="signup"),
    url(r'^thanks/$', views.HomePage.as_view(), name='thanks'),
    url(r'^loggedin/$',views.HomePage.as_view(),name='test'),
]
