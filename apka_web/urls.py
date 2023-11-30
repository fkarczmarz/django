from django.urls import path
from .views import todolistResponse
from . import views
urlpatterns = [
    path('todolist/', todolistResponse),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/new/', views.task_new, name='task_new'),
    path('tasks/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('tasks/<int:pk>/toggle_completed/', views.toggle_task_completed, name='toggle_task_completed'),

]