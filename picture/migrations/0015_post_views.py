# Generated by Django 3.1.2 on 2020-10-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0014_review_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
