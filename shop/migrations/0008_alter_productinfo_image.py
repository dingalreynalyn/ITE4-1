# Generated by Django 4.1.5 on 2023-01-12 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_productinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='image',
            field=models.ImageField(upload_to='shop/static/'),
        ),
    ]
