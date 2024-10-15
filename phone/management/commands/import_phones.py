import csv
from django.core.management.base import BaseCommand
from phone.models import Phone
from slugify import slugify
from pathlib import Path
import os

class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def handle(self, *args, **options):
        path = os.path.abspath('phones.csv')
        print(os.path.exists(path))  # Проверка существования файла

        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                slug = slugify(row['name'])  # Генерация slug

                # Создание объекта Phone (то, что Вам нужно)
                phone = Phone(
                    id=row['id'],  # Не забудьте про преобразование типов, если нужно
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists'] == 'True',  # Преобразование строки в булевый тип
                    slug=slug
                )
                print(phone)
                phone.save()  # Сохранение в базу данных
