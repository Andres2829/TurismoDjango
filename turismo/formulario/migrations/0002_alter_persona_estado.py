# Generated by Django 3.2.8 on 2022-06-14 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='estado',
            field=models.CharField(default='PENDIENTE', max_length=150),
        ),
    ]
