from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'search'

urlpatterns = [
    url(r'^$', views.result, name='result')
    # path('', views.index, name='index')
    ]

