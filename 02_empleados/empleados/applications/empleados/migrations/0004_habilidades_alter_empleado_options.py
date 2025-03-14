# Generated by Django 5.1 on 2024-09-03 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_alter_empleado_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=60, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades Empleados',
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
    ]
