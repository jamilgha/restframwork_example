from django.urls import path
from . import views

appname='api'
urlpatterns=[

    path('',views.apiOverview,name='api-overviwe'),
    path('task-list/',views.Tasklist,name='task-list'),
    path('task-detail/<str:pk>/',views.taskdetail,name='task-detail'),
    path('task-update/<str:pk>/',views.updateTask,name='task-update'),
    path('task-delete/<str:pk>/',views.deleteTask,name='task-delete'),
]