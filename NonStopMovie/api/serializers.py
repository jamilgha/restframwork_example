from rest_framework import serializers
from .models import movie


class Movieserializers(serializers.ModelSerializer):
    class Meta:
        model=movie
        fields='__all__'