from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial')
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='images.image'),
        ),
    ]

