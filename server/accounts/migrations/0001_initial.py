# Generated by Django 4.1.2 on 2023-01-18 15:48

from django.db import migrations
#используем явный призыв модели
from accounts.models import User
def create_default_user(apps, schema_editor):
    #return model with help first app - 'accounts', second model - 'AccountUser'
    #ленивый призыв модели
    #AccountUser = apps.get_model('accounts', 'AccountUser')
    usr = User(username='Oleg')
    usr.set_password('rava18')
    usr.save()

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_default_user, lambda x, y: (x, y))
    ]
