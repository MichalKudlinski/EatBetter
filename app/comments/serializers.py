import sys

from rest_framework import serializers
from core.models import Comment

sys.path.append("..")


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id','user','comment_date','text','recipe','rate']
        read_only_fields = ['id','user','comment_date']

