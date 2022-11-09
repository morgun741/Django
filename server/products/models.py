from django.db import models

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE(K))
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    def __str__(self):
        return self.name