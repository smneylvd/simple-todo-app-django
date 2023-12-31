from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login',views.login),
    path('logout', views.logout),
    path('register',views.register),

    path('addTask', views.addTask),
    path('deleteTask/<int:task_id>', views.deleteTask)
]