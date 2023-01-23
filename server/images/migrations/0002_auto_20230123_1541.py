from django.db import migrations
from django.core.files import File

def create_default_image(apps, shema_editor):
    file_name = 'images/орех.jpg'
    # берём модель поступаемого apps
    # это ленивая подгрукзка модели
    Image = apps.get_model('images', 'image')
    # проявляем в модели значения fields
    img = Image.objects.create(
        title = 'default',
        value = file_name
    )
    #сохраняем значение во fields, соответствующей таблицы, first argument will be file name, second - explicit(явное) betoken
    # path to file in File, 'rb' - opening file in binary mode
    img.value.save(file_name, File(open('images/fixtures/images/орех.jpg', 'rb')))

class Migration(migrations.Migration):
    #it let me betoken other dependencies, but now we don't use another models
    dependencies = [
        ('images', '0001_initial'),
    ]

    # the object migrations.RunPython() actuate the python code
    # second argument here must to be function wich amend mistakes first, but now she doesn't need
    operations = [migrations.RunPython(create_default_image, lambda x, y: (x, y))
    ]
