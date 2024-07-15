# Generated by Django 5.0.6 on 2024-07-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0041_order_order_track_alter_address_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_track',
            field=models.CharField(blank=True, choices=[(1, 'Order Placed'), (2, 'Shipped'), (3, 'Reaches at Ahmedabad'), (4, 'Delivered')], default=1, max_length=50, null=True),
        ),
    ]
