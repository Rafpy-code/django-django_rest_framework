# Generated by Django 5.1 on 2024-09-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_remove_empleado_apellido_alter_empleado_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='image',
            field=models.ImageField(upload_to='empleados_img', verbose_name='Foto'),
        ),
    ]
