# Generated by Django 3.1.2 on 2020-10-16 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0008_auto_20201016_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(default=''),
        ),
    ]