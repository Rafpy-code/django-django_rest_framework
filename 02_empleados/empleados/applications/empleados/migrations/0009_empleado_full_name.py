# Generated by Django 5.1 on 2024-09-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0008_alter_empleado_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, editable=False, max_length=120, verbose_name='Nombre Completo'),
        ),
    ]
