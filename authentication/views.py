from django.shortcuts import render
from jwt.exceptions import ExpiredSignatureError
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .authserializer import authSerializer
from .models import userAbstract
import jwt, datetime


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = authSerializer(data=request.data)
    if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_puppy(request):
    email = request.data['email']
    password =request.data['password']
    user = userAbstract.objects.filter(email=email).first()
    if user is None:
        raise AuthenticationFailed('user not found')
    if not user.check_password(password):
        raise AuthenticationFailed('invalid credential')
    
    payload = {
        'id': user.id,
       
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    } 

    token = jwt.encode(payload, 'secret', algorithm='HS256')
    response =  Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        "message": "success",
        'jwt': token,
     
    }
    
    return response


class userView(APIView):
    def currentuser(request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('unauthenticated')
        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
            
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('unauthenticated')
        user = userAbstract.objects.filter(id=payload['id']).first()
        serializers = authSerializer(user)
        return Response(serializers.data)
        
@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        "message": "success logout",      
    }
    return response