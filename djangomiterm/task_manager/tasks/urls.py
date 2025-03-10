from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='Task_List'),
    path('AddTask/', views.add_task, name='AddTask'),
    path('AddTask/save/', views.save_task, name='SaveTask'),
    path('editTask/<int:id>/', views.edit),
    path('editTask/<int:id>/updateTask/', views.update),
    path('confirmDelete/<int:id>/', views.confirm_delete),
    path('confirmDelete/<int:id>/delete_task/', views.deleteTask),
    path('search/', views.task_search, name='task_search'),
]