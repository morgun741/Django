from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ForeignKey('images.Image',on_delete=models.PROTECT, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    #импортированная AbstractUser уже содержит все поля доступные пользователю
    #мы производим только расширение этой модели за счёт предидущих полей
    #ниже указанная функция вернёт username(имеющийся в AbstractUser) при преходе на который мы найдём выше указанные поля

    def __str__(self):
        return self.username
