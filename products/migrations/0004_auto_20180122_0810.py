# Generated by Django 2.0.1 on 2018-01-21 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180121_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagePath',
            field=models.ImageField(default='No_imange_yet', upload_to='products/vitamins/images'),
        ),
    ]
