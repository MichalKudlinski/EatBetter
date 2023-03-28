from django.contrib import admin

from .models import Product, User,Tag,Ingredient,Recipe

# Register your models here.
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Tag),
admin.site.register(Ingredient),
admin.site.register(Recipe)