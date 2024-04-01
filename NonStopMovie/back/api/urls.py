from django.urls import path
from . import views

appname="api"
urlpatterns=[
    path('', views.apiOverview, name='api-overviwe'),
    path('movie-list/', views.Movie_list, name=' Movie List'),
    path('movie-detail/<str:id>/', views.Movie_detail, name='Movie Detail'),
    path('movie-create/', views.Movie_create, name='Movie Create'),
    path('movie-update/<str:pk>', views.Movie_Update, name='Movie update'),
    path('slider_lsit/', views.sliders, name='slier list'),
]

