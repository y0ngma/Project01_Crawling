from django.urls import path
from . import views

urlpatterns = [

path('list',             views.list,           name='list'),
path('service3',         views.service3,       name='service3'),
path('service4',         views.service4,       name='service4'),



]