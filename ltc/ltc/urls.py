"""ltc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ltccell import views as ltccell_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',ltccell_views.home,name='home'),
    url(r'^login/',ltccell_views.login,name='login'),
    url(r'^adminlogin/',ltccell_views.adminlogin,name='adminlogin'),
    url(r'^adminlogin1/',ltccell_views.adminlogin1,name='adminlogin1'),
    url(r'^adminlogged/',ltccell_views.adminlogged,name='adminlogged'),
    url(r'^login1/',ltccell_views.login1,name='login1'),
    url(r'^logged/',ltccell_views.logged,name='logged'),
    url(r'^advance/',ltccell_views.advance,name='advance'),
    url(r'^advance1/',ltccell_views.advance1,name='advance1'),
    url(r'^drawn/',ltccell_views.drawn,name='drawn'),
    url(r'^claim/',ltccell_views.claim,name='claim'),
    url(r'^claim2/',ltccell_views.claim2,name='claim2'),
    url(r'^claimed/',ltccell_views.claimed,name='claimed'),
    url(r'^register/',ltccell_views.register,name='register'),
    url(r'^register1/',ltccell_views.register1,name='register1'),
    url(r'^registered/',ltccell_views.registered,name='registered')
]
