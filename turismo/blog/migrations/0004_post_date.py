# Generated by Django 3.2.8 on 2022-06-13 22:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
