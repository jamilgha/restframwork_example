from django.contrib import admin
from .models import movie,moviegender,movie_company,slider_home
# Register your models here.
admin.site.register(movie)
admin.site.register(moviegender)
admin.site.register(movie_company)
admin.site.register(slider_home)