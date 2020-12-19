  
import datetime
from .serializers import UserSignupSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from .models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status, serializers, authentication
from rest_framework.authtoken.models import Token

class UserSignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Successfully Created, Please Sign-In`',
            'data': response.data
        })