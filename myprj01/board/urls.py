from django.urls import path
from . import views

urlpatterns = [
    path('service3', views.service3, name='service3'),

    
]
