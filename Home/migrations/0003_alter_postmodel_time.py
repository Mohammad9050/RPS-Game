# Generated by Django 4.0.1 on 2022-01-23 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_postmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
