# Generated by Django 3.1.2 on 2020-10-19 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0019_post_posted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posted_by',
            field=models.CharField(max_length=30),
        ),
    ]
