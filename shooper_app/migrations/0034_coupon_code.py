# Generated by Django 5.0 on 2024-04-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0033_add_to_cart_size_alter_add_to_cart_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='coupon_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('discount', models.IntegerField()),
            ],
        ),
    ]
