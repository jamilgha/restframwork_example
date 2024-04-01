from rest_framework import serializers
from .models import movie,slider_home


class Movieserializers(serializers.ModelSerializer):
    class Meta:
        model=movie
        fields='__all__'
class sliderSerializers(serializers.ModelSerializer):
    class Meta:
        model=slider_home
        fields='__all__'