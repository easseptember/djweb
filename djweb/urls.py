"""djweb URL Configuration

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
from djwebs import views as djwebs_views  # new
from djwebs import add   as djwebs_add  # new
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^init/', djwebs_views.init),
    url(r'^index/', djwebs_views.index),
    url(r'^add/', djwebs_add.add),
    url(r'^hand/', djwebs_add.hand),
    url(r'^delete/', djwebs_add.delete),
    url(r'^update/', djwebs_add.update),
    url(r'^handupdate/', djwebs_add.handupdate),
]
