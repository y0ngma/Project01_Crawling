from django.urls import path
from . import views

urlpatterns = [

path('service2',         views.service2,       name='service2'),
path('service3',         views.service3,       name='service3'),
path('service4',         views.service4,       name='service4'),
path('test',         views.test,       name='test'),



]