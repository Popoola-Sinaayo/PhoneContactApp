from msilib.schema import ListView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('all', views.ListView.as_view())
]
