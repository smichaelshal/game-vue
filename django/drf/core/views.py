from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from rest_framework import generics
from .serializers import UserSerializer, RegisterSerializer
from rest_framework import serializers

from .models import Life
from django.contrib.auth.models import User

from rest_framework import status
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated   


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'msg': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'msg': 'Username or password is incorrect.'},
                        status=HTTP_400_BAD_REQUEST)
    
    listToken = Token.objects.all().filter(user=user)
    if len(listToken) != 0:
        return Response({'msg': 'The user is already logged in.'},
                        status=HTTP_400_BAD_REQUEST)


    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': request.headers["Authorization"].split(' ')[1]}
    # [Authorization]
    
    return Response(data, status=HTTP_200_OK)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = request.data['password']
        password2 = request.data['password2']
        if password != password2:
            raise serializers.ValidationError({'msg':'Passowrd must match.'})

        user = serializer.save()
        tempLife = Life(user=user, number=10)
        tempLife.save()
        return Response({"msg": "You have successfully registered"})

class LogoutAPI(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        strTokenUser = request.headers["Authorization"].split(' ')[1]
        user = Token.objects.all().filter(key=strTokenUser)[0].user
        user.auth_token.delete()
        return Response({"msg": "User logged in successfully."})


from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated 

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    
    serializer_class = ChangePasswordSerializer
    model = User
    # permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        strTokenUser = request.headers["Authorization"].split(' ')[1]
        user = Token.objects.all().filter(key=strTokenUser)[0].user

        self.object = user
        serializer = self.get_serializer(data=request.data)
        print("aaaa0", request.data)
        if serializer.is_valid():
            # Check old password
            print("aaaa1", serializer.data.get("old_password"))
            if not self.object.check_password(serializer.data.get("old_password")):
                print("aaaa2")
                return Response({"old_password": ["Wrong password."]}, status=HTTP_400_BAD_REQUEST)
            print("aaaa3")
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            print("aaaa4")
            self.object.save()
            print("aaaa5")
            response = {
                'status': 'success',
                'code': HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            print("aaaa6")
            return Response(response)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
# ----------------------------------------------------------------------------------------
class LifeAPI(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        strTokenUser = request.headers["Authorization"].split(' ')[1]
        user = Token.objects.all().filter(key=strTokenUser)[0].user
        usernameToAttack = request.data["toattack"]

        userToAttack=User.objects.all().filter(username=usernameToAttack)[0]
        lifeUserToAttack = Life.objects.all().filter(user=userToAttack)[0]

        if lifeUserToAttack.number != 0:
            lifeUserToAttack.number = lifeUserToAttack.number - 1
            lifeUserToAttack.save()

        return Response({"life": lifeUserToAttack.number})

    def get(self, request, *args, **kwargs):
        strTokenUser = request.headers["Authorization"].split(' ')[1]
        user = Token.objects.all().filter(key=strTokenUser)[0].user

        listLife = Life.objects.all()
        dictData =  {}

        for tempUser in listLife:
            dictData[tempUser.user.username] = tempUser.number
        return Response(dictData)

        # return Response({"msg": "User logged in successfully."})
        # Token.objects.all().filter(key="34ac5679ff32fa927660d471cc585635f12f7a07")[0].user
