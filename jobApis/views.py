from rest_framework.generics import GenericAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import  IsAuthenticated
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

    @action(methods= ['get'], detail=False)
    def newest(self, request):
        newest= self.get_queryset().order_by('created').last()
        serializer=self.get_serializer_class()(newest)
        return Response(serializer.data)

class JobList(APIView):
    def get(self,request,format = None):
        all_jobs = Job.objects.all()
        serializerdata = JobSerializer(all_jobs,many = True)
        return Response(serializerdata.data)
    
    permission_classes=[IsAuthenticated]
    def post(self, request, format=None):
        job= request.data
        serializerdata=JobSerializer(data=request.data)
        if serializerdata.is_valid():
            serializerdata.save()
            return Response(serializerdata.data, status.HTTP_201_CREATED)
        return Response(serializerdata.errors, status=status.HTTP_400_BAD_REQUEST)


class jobDelete(DestroyAPIView):
    pass
