from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
router = SimpleRouter()
router.register('user-profiles', views.UserProfileViewSet,basename = 'user-profiles')

app_name= 'user_profiles'

urlpatterns =[
    path('',include(router.urls))
]