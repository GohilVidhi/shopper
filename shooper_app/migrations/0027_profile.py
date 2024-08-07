# Generated by Django 5.0 on 2024-04-24 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0026_rating_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=60)),
                ('address', models.TextField()),
            ],
        ),
    ]
