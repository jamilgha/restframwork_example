from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
from .models import Task
# Create your views here.
@api_view(['Get','POST'])
def apiOverview(request):
    api_urls={
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)
@api_view(['GET'])
def Tasklist(request):
    tasks=Task.objects.all()
    serializer=TaskSerializers(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskdetail(request,pk):
    tasks=Task.objects.get(id=pk)
    serializer=TaskSerializers(tasks,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def createTask(request):
    serializer=TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return  Response(serializer.data)
@api_view(['POST'])
def updateTask(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializers(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return  Response(serializer.data)
@api_view(['DELETE'])
def deleteTask(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return Response('The Items Has Delete')