# Generated by Django 4.0.1 on 2022-02-15 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='name',
            field=models.CharField(default='Undefined', max_length=40),
        ),
    ]
