from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Index,name='index'),
    path('adminuser/',AdminUser,name='admin'),
    path('user/',Users,name='user'),
    path('task/',NewTask,name='task'),
]
