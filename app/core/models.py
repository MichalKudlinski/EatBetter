import sys
import uuid
import os
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver





def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'recipe', filename)

class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and  return a new user."""
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return new superuser"""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User in the system.
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'


class Product(models.Model):
    name = models.CharField(max_length=255, unique = True)
    calories = models.IntegerField()
    total_fat = models.FloatField()
    protein = models.FloatField()
    carbohydrate = models.FloatField()
    sugars = models.FloatField()
    fiber = models.FloatField()
    nutrition_score = models.FloatField()


class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    name = models.CharField(max_length = 255)
    description = models.TextField(blank = True)
    healthy_products = models.ManyToManyField('Product')
    ingredients = models.ManyToManyField('Ingredient')
    time_minutes = models.IntegerField()
    tags = models.ManyToManyField('Tag')
    prize = models.FloatField()
    image = models.ImageField(null = True, upload_to = recipe_image_file_path)

    def __str__(self):
        return self.name
    


class Tag(models.Model):
    """Tag for filtering recipes."""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete= models.CASCADE)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient for recipes."""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user")
    recipies = models.ManyToManyField(Recipe, default=None, blank=True)

@ receiver(post_save, sender=User)
def UserProfileCreator(sender, instance=None, created=False, **kwargs):
    if created:
        UserProfile.objects.create(
            user=instance)

        