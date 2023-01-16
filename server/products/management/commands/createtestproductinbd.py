from django.core.management.base import BaseCommand, CommandError
from products.models import Product

#создаидим класс для перечисления имеющихся аргументов в командной строке
class Command(BaseCommand):
    # создадим django-метод hande в котором и будет содержаться вся логика
    #создаваемой команды
    #в кочестве аргументов этот  метод будет принимать контекст
    #а также набор именованых и перечисляемых атребутов(**kwargs)
    def handle(self, *args, **kwargs):
        try:
            for idx in range(1, 10):
                product_name = '[test]-product-%s' % idx
                Product.objects.create(name=product_name)
                self.stdout.write(self.style.SUCCESS(product_name))
        except Exception as err:
            raise CommandError(err)