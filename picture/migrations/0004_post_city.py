# Generated by Django 3.1.2 on 2020-10-16 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0003_auto_20201016_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(default='', max_length=30),
        ),
    ]
