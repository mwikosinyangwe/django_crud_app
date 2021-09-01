from django.urls import path
from . import views

urlpatterns = [
    
    
    path('', views.home, name='home'),
    path('todo_detail/<str:pk>/', views.detail_view, name='todo_detail'),
    path('todo_update/<str:pk>/', views.todo_update, name='todo_update'),
    path('todo/<int:pk>', views.DeleteTodo, name='delete'),
]