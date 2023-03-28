from rest_framework import serializers
from core.models import UserProfile
from recipe.serializers import RecipeSerialzier
from users.serializers import UserSerializer
import sys

sys.path.append("..")

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required = True)
    recipes = RecipeSerialzier(many = True, required = False)
    

    class Meta:
        model = UserProfile
        fields = ['user','recipes']
