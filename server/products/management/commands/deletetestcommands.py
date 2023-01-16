from django.core.management.base import BaseCommand, CommandError
from products.models import Product

class Command(BaseCommand):

    def handle(self, *args, **option):
        try:
               #функция filter возьмёт из таблицы все элементы, соответствующие условию name__startswith='[test]'
               query=Product.objects.filter(name__startswith='[test]')
               query.delete()
               self.stdout.write(self.style.SUCCESS('всё норм'))
        except Exception as err:
            raise CommandError(err)