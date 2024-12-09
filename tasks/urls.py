

from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_task, name='add_task'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),

]