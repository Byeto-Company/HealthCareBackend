from django.core.management.base import BaseCommand
from customer.factory import CustomerFactory

class Command(BaseCommand):
    help = 'Generate fake customers'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of customers to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for _ in range(total):
            CustomerFactory.create()
        self.stdout.write(self.style.SUCCESS(f'{total} customers created successfully!'))