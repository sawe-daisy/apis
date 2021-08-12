from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, JobSerializer
from rest_framework.response import Response
from rest_framework import permissions, serializers
from rest_framework import status
from .models import User, Job
from django.contrib.auth import login
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.conf import settings
from django.contrib import auth
import jwt
# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class jobViewSet(viewsets.ModelViewSet):
    queryset= Job.objects.all()
    serializer_class=JobSerializer

    @action(methods= ['get', 'post'], detail=False)
    def newest(self, request):
        newest= self.get_queryset().order_by('-created').last()
        serializer=self.get_serializer_class()(newest)
        return Response(serializer.data)
