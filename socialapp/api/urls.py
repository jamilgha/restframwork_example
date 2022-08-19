from django.urls import path
from . import views
appname="api"
urlpatterns = [

    path('user/', views.user_list,name='user List'),
]
