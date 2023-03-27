import sys

from core.models import Product

from .data import foods_final

sys.path.append("..")

def get_data_into_model():
    for el in foods_final.values:
        name = el[1]
        calories = el[2]
        total_fat = el[3]
        protein = el[4]
        carbohydrate = el[5]
        sugars = el[6]
        fiber = el[7]
        nutrition_score = el[8]
        Product.objects.create(name = name, calories = calories, total_fat =total_fat,
                           protein = protein, carbohydrate = carbohydrate, sugars =sugars, fiber= fiber,
                           nutrition_score = nutrition_score)

