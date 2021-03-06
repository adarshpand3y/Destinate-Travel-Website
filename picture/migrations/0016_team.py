# Generated by Django 3.1.2 on 2020-10-18 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0015_post_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='', upload_to='images')),
                ('description', models.TextField()),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
    ]
