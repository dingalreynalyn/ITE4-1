# Generated by Django 4.1.5 on 2023-01-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopproducts',
            name='size',
            field=models.CharField(default='M/L/X/XL', max_length=255),
            preserve_default=False,
        ),
    ]
