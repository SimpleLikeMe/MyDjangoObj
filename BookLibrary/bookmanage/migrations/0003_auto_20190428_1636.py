# Generated by Django 2.2 on 2019-04-28 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanage', '0002_auto_20190428_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
