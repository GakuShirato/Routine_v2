from django.urls import path
from todo import views

urlpatterns = [
    path('', views.ListTask, name="list_task"),
    path('update_task/<str:pk>/', views.UpdateTask, name="update_task"),
    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"),
]
