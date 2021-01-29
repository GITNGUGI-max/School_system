from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Students,Course, Fee
from .serializers import StudentSerializer, CourseSerializer, FeeSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer   

class FeeViewSet(viewsets.ModelViewSet):

    queryset = Fee.objects.all()
    serializer_class = FeeSerializer   


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

