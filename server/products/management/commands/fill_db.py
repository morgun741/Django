from django.core.management.base import BaseCommand, CommandError
from products.models import Product
# определение аргументов команды в командной строке
# заместо parser в функцию пойдёт ArgumentParser(см. модуль argparse)
def add_arguments(self, parser):
    #добавляем аргумент, который наз. 'range'(количество созд. записей)
    parser.add_argument('--range', type=int, required=False, default=10)

class Command(BaseCommand):
    # определение аргументов команды в командной строке
    # заместо parser в функцию пойдёт ArgumentParser(см. модуль argparse)
    def add_arguments(self, parser):
        # добавляем аргумент, который наз. 'range'(количество созд. записей)
        # parametr required(обязательный)=False talk about that the default-value don't necessary
        # '--range' to write strictly(строго)
        parser.add_argument('--range', type=int, required=False, default=10)
    # why is option? Because here will be store options which pass through the command line
    def handle(self, *args, **option):
        try:
           for idx in range(1, option.get('range')+1):
               product_name = '[test]-product-%s' % idx
               Product.objects.create(name=product_name)
               self.stdout.write(self.style.SUCCESS(product_name))
        except Exception as err:
            raise CommandError(err)


