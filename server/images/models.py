from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=150)
    value = models.ImageField(upload_to='images')
    # мы будем возвращать url-адресс, ведущий на необходимое нам изображение
    def __str__(self):
        return self.value.url