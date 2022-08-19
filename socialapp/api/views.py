
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import user
from .serializers import Userserializers
# Create your views here.
@api_view(['GET'])
def user_list(request):
    movie_list=user.objects.all()
    serializers=Userserializers(movie_list,many=True)

    return  Response(serializers.data)

