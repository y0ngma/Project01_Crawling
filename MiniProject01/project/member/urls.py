from django.urls import path
from . import views

urlpatterns = [
    # path('write',   views.write,  name = 'write'),
    # path('edit',    views.edit,   name = 'edit'),
    # path('list',   views.list,  name = 'list'),
    # path('member',  views.member, name = 'member'),
    # path('delete',  views.delete, name = 'delete'),
    # path('login',   views.login,  name = 'login'),
    # path('logout',  views.logout, name = 'logout'),
    path('join',    views.join,   name = 'join'),
    path('index',   views.index,  name = 'index'),
    

]