import csv
from django.core.management.base import BaseCommand
from gestion_inmuebles.models import Pais

# Se ejecuta usando python manage.py test_client

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/pais.csv', 'r')
        reader = csv.reader(archivo, delimiter=';')
        next(reader) # Se salta la primera linea
        for fila in reader:
                Pais.objects.create(id=fila[0], nombre=fila[1])