import sys
from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from core.models import UserProfile
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
# Create your views here.

sys.path.append("..")

class UserProfileViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):
    quseryset = UserProfile.objects.all()
    serializer_class  = UserProfile
    permission_classes = IsAuthenticatedOrReadOnly
    authentication_classes = TokenAuthentication

    @action(methods = ['patch','get'], detail = True)
    def my_profile(self,request):
        queryset = UserProfile.objects.filter(user = self.request.user).get()
        serializer = self.get_serializer(queryset)

        return Response(serializer.data)


