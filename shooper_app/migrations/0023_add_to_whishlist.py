# Generated by Django 5.0 on 2024-04-03 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0022_alter_product_star'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_to_whishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shooper_app.product')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shooper_app.user')),
            ],
        ),
    ]
