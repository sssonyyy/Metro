from django.contrib import admin
from django.urls import path

from metroApp.views import *

urlpatterns = [
    path('',  home, name='home'),
    path('info/', info, name='info'),
    path('drivers/', drivers, name='drivers'),
    path('spravka/<slug:slug>', spravkaM, name='spravka'),
    path('schema/', schema, name='schema'),
    path('contacts/', contacts, name='contacts'),
    path("create/", create),
    path("add/", add, name="add"),
    path('delete/', delete_object_function, name='delete'),


]