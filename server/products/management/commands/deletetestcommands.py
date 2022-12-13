from django.core.management.base import BaseCommand, CommandError
from products.models import Product

class Command(BaseCommand):

    def handle(self, *args, **option):
        try:
               query=Product.objects.filter(name__startswith='[test]')
               query.delete()
               self.stdout.write(self.style.SUCCESS('всё норм'))
        except Exception as err:
            raise CommandError(err)