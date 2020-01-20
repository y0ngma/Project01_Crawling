from django.urls import path
from . import views

urlpatterns = [
#    path('write',   views.write,  name = 'write'),
    # path('index',   views.index,  name = 'index'),
    # path('list',   views.list,  name = 'list'),
    # path('member',  views.member, name = 'member'),
    path('join',    views.join,   name = 'join'),
#    path('edit',    views.edit,   name = 'edit'),
    path('delete',  views.delete, name = 'delete'),
    path('login',   views.login,  name = 'login'),
    path('logout',  views.logout, name = 'logout'),
    

]