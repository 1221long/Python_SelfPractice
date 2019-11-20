import json

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from demo.models import User
from demo.serializer import UserSerializer


@api_view(['GET','POST'])
def User_list(request):
    if request.method=="GET":
        users = User.
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        #print(request.body)
        serializer = UserSerializer(data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE']) #
def User_detial(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = UserSerializer(user,data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)