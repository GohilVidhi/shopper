# Generated by Django 5.0 on 2024-02-13 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.IntegerField(max_length=6, null=True),
        ),
    ]
