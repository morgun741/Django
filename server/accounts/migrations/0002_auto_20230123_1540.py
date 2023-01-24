from django.db import migrations
#используем явный призыв модели
from accounts.models import User

def create_default_user(apps, schema_editor):
    #return model with help first app - 'accounts', second model - 'AccountUser'
    #ленивый призыв модели
    #AccountUser = apps.get_model('accounts', 'AccountUser')
    usr = User(username='Oleg',
    #to give access user for admin-panel
               is_staff=True,
    #to give user all possible rules
               is_superuser=True)
    usr.set_password('rava18')
    usr.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_user, lambda x, y: (x, y))
    ]
