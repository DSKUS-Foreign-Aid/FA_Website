from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Adds the GDP data'
    def get_data(self):
        pass