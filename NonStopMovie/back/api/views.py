from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import movie,slider_home
from .serializers import Movieserializers,sliderSerializers

# Create your views here.
@api_view(['Get','POST'])
def apiOverview(request):
    api_urls={
        'List':'/movie-list/',
        'Detail Movie':'/Movie-detail/<str:pk>/',
        'Create Movie':'/Movie-create/',
        'Update Movie':'/Movie-update/',
        'Delete Movie':'/Movie-delete/<str:pk>/',
        'slider List':'/slider_lsit/',
    }
    return Response(api_urls)
@api_view(['GET'])
def Movie_list(request):
    movie_list=movie.objects.all()
    serializers=Movieserializers(movie_list,many=True)

    return  Response(serializers.data)


@api_view(['GET'])
def Movie_detail(request,id):
    Movie_detail=movie.objects.get(id=id)
    serializer=Movieserializers(Movie_detail,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def Movie_create(request):
    serializer=Movieserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def Movie_Update(request,pk):
    movie_update=movie.objects.get(id=pk)
    serializer=Movieserializers(instance=movie_update,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def sliders(request):
    slider_list=slider_home.objects.all()
    serializer=sliderSerializers(slider_list,many=False)
    return Response(serializer.data)