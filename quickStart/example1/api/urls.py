from django.urls import path
from . import views

appname='api'
urlpatterns=[

    path('',views.apiOverview,name='api-overviwe')
]