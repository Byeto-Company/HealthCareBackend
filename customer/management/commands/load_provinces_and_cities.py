import json
from django.core.management.base import BaseCommand
from customer.models import Province, City


class Command(BaseCommand):
    help = 'Load provinces and cities from a JSON file'

    def handle(self, *args, **kwargs):
        with open('customer/management/commands/provs.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            for province_data in data:
                province_name = province_data['name']
                province, created = Province.objects.get_or_create(name=province_name)

                for city_data in province_data['cities']:
                    City.objects.get_or_create(
                        name=city_data['name'],
                        province=province,
                        latitude=city_data['latitude'],
                        longitude=city_data['longitude']
                    )
        self.stdout.write(self.style.SUCCESS('Successfully loaded provinces and cities'))
