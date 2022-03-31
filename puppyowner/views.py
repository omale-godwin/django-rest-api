from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .models import PupOwnerRegistration, Puppy, EmdeeContact, EmdeeBlog
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PupOwnerRegistrationSerializer, BookedAppsSerializer, PuppySerializer, contactSerializer, EmdeeBlogSerializer

# Create your views here.
# def pup_owner_registration_lists(request):
#     info = PupOwnerRegistration.objects.all()

def show_pups(request):
    return JsonResponse('omale agin', safe=False)
    
@api_view(['GET', 'POST'])
def all_pups(request):
    url_pat = {
        'create': "creating",
        'update': "updating",
        "view": 'viewingSingle',
        'delete': 'deleting'
    }
    return Response(url_pat)
    
@api_view(['GET'])
# @permission_classes([AllowAny])
def all_pups(request):
    info = Puppy.objects.all()
    serializer = PuppySerializer(info, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def emdee_blog(request):
    info = EmdeeBlog.objects.all()
    serializer = EmdeeBlogSerializer(info, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([AllowAny])
def puppy_detial(request, pk):
    info = Puppy.objects.get(id=pk)
    serializer = PuppySerializer(info, many=False)
    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([AllowAny])
def puppy_post(request):
    serializer = PuppySerializer(data=request.data)
    if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
# @permission_classes([AllowAny])
def emdeecontact(request):
    serializer = contactSerializer(data=request.data)
    if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
# @permission_classes([AllowAny])
def puppy_update(request, pk):
    info = Puppy.objects.get(id=pk)
    serializer = PuppySerializer(info, data=request.data)
    if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([AllowAny])
def puppy_delete(request, pk):
    info = Puppy.objects.get(id=pk)
    delinfo = info.delete()
    if(delinfo):
       return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)