from django.contrib import admin
from portal.models import Students, Classes, Course, Teachers, Fee, Timetable

# Register your models here.

admin.site.register(Students)
admin.site.register(Classes)
admin.site.register(Course)
admin.site.register(Teachers)
admin.site.register(Fee)
admin.site.register(Timetable)
