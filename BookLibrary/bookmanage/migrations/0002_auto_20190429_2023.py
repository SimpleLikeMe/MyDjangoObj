# Generated by Django 2.2 on 2019-04-29 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
