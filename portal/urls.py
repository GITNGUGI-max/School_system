
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from portal import views



router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'fees', views.FeeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path(r'^api-auth/', include('rest_framework.urls', namespace='framework'))
    
]
