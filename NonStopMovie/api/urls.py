from django.urls import path
from . import views

appname="api"
urlpatterns=[
    path('', views.apiOverview, name='api-overviwe'),
    path('movie-list/', views.Movie_list, name='api-movie-list'),
]