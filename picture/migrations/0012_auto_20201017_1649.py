# Generated by Django 3.1.2 on 2020-10-17 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0011_reviews_subscribe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]
