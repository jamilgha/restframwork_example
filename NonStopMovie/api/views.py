from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import movie
from .serializers import Movieserializers

# Create your views here.
@api_view(['Get','POST'])
def apiOverview(request):
    api_urls={
        'List':'/movie-list/',
        'Detail Movie':'/Movie-detail/<str:pk>/',
        'Create Movie':'/Movie-create/',
        'Update Movie':'/Movie-update/',
        'Delete Movie':'/Movie-delete/<str:pk>/',
    }
    return Response(api_urls)
@api_view(['GET'])
def Movie_list(request):
    movie_list=movie.objects.all()
    serializers=Movieserializers(movie_list,many=True)

    return  Response(serializers.data)





