# Generated by Django 5.0 on 2024-04-01 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0019_remove_product_color1_product_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price1',
            field=models.CharField(blank=True, choices=[('0', '500'), ('500', '3000'), ('3000', '10000'), ('10000', '40000'), ('40000', '60000')], max_length=50, null=True),
        ),
    ]