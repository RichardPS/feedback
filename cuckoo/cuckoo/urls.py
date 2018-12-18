"""cuckoo URL Configuration"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^backoffice/', admin.site.urls),
    url(r'^', include('survey.urls'))
]
handler404 = 'survey.views.page_not_found'
