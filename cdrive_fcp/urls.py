"""cdrive_fcp URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views import static
from django.views.generic.base import RedirectView

from core import views as core_view

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^', include('core.urls')),
    url(r'^', include('game.urls')),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^.*$', RedirectView.as_view(pattern_name='homepage'), name='index')
]

