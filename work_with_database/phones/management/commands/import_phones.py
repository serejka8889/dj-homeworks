import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Импортирует телефоны из CSV файла'

    # Добавление аргументов командной строки
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Путь к CSV файлу')

    # Открывает CSV файл, обрабатываем и добавляем данные в базу
    def handle(self, *args, **options):
        
        file_path = options['file_path'] 

        try:
            with open(file_path, newline='', encoding='utf-8') as file:
                phones = list(csv.DictReader(file, delimiter=';'))

            for phone in phones:
                data = {
                    'id': int(phone['id']), 
                    'name': phone['name'], 
                    'price': float(phone['price'].replace(',', '.')),
                    'image': phone['image'],
                    'release_date': phone['release_date'],
                    'lte_exists': True if phone['lte_exists'] == 'True' else False,
                    'slug': phone['name'] 
                }

                # Создание записи (обновление в базе)
                created = Phone.objects.update_or_create(id=data['id'], defaults=data)

                if created:
                    self.stdout.write(f"Телефон '{data['name']}' успешно создан.")
                else:
                    self.stdout.write(f"Телефон '{data['name']}' уже существует.")

        except FileNotFoundError:
            self.stderr.write("Файл не найден. Проверьте правильность указанного пути.")
        except Exception as e:
            self.stderr.write(f"Произошла ошибка: {e}")

