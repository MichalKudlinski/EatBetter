import sys

from core.models import Product

from .data import foods_final

sys.path.append("..")

def get_data_into_model():
    for el in foods_final:
        name = el['name']
        calories = el['calories']
        total_fat = el['total_fat']
        protein = el['protein']
        carbohydrate = el['carbohydrate']
        sugars = el['sugars']
        fiber = el['fibers']
        nutrition_score = el['nutrition_score']
        Product.objects.create(name = name, calories = calories, total_fat =total_fat,
                           protein = protein, carbohydrate = carbohydrate, sugars =sugars, fiber= fiber,
                           nutrition_score = nutrition_score)

