from rest_framework import serializers
from .models import Students, Course, Fee

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=Students
        fields = ['id', 'firstName', 'middleName', 'surname', 'regNumber', 'email', 'gender', 'birthDate', 'course', 'yearOfStudy']

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=Course
        fields = ['id', 'courseName', 'level']

class FeeSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=Fee
        fields = ['id', 'student', 'yearofStudy', 'amount', 'dueDate', 'balance', 'overPayment' ]


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

        extra_kwargs = {'password': {'write_only':True, 'required':True}} 


        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user




