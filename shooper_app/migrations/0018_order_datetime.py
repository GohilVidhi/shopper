# Generated by Django 5.0 on 2024-03-28 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0017_rename_img_order_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='datetime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
