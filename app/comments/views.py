import sys
from django.shortcuts import render
from rest_framework.viewsets import mixins, GenericViewSet
from core.models import Comment
from . import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

sys.path.append("..")
# Create your views here.




class CommentsViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet):

    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]



    def perform_create(self,serializer):
        serializer.save(user = self.request.user)