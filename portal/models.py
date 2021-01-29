from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    courseName=models.CharField(max_length=1000)
    level = models.CharField(max_length=100, null=True)

    def __str__(self):

        return self.courseName + "-" + self.level
    
class Students(models.Model):
    
    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    regNumber= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    birthDate = models.DateField()
    course = models.CharField(max_length=1000, default='')
    yearOfStudy = models.IntegerField(default=1)



class Classes(models.Model):
    classStudentId = models.CharField(max_length=100)
    className = models.CharField(max_length=100)
    classRoom = models.CharField(max_length=100)
    classType = models.CharField(max_length=100)

class Teachers(models.Model):
    firstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Timetable(models.Model):
    time = models.TimeField()
    date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.CharField(max_length=100)

class Fee(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, null=False, blank=False)
    yearofStudy = models.IntegerField(default="1")
    amount = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='USD')
    dueDate = models.DateField()
    balance = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='USD')
    overPayment = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='USD')
    
    
class RegisterForm(models.Model):

    email = models.EmailField()
    

    
    





   


