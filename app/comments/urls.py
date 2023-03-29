from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()

router.register('comments',views.CommentsViewSet)

app_name = 'comments'
urlpatterns =[
    path('',include(router.urls))
]