from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('query/',query,name='query'),
    path('delete/<int:pk>',delete,name='delete'),
    path('update/<int:pk>',update,name='update'),
    path('edit/<int:pk>',edit,name='edit')
]
