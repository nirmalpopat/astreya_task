from django.urls import include, path
from . import views
from django.contrib.auth import login

urlpatterns = [
    path('', views.index, name='index')
]
