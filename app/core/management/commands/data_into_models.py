from django.core.management.base import BaseCommand
from utils.data_into_models import get_data_into_model


class Command(BaseCommand):
    get_data_into_model()