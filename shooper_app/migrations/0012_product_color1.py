# Generated by Django 5.0.2 on 2024-03-09 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shooper_app', '0011_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shooper_app.color'),
        ),
    ]
