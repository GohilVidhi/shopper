# Generated by Django 5.0 on 2024-02-16 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0003_alter_user_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]