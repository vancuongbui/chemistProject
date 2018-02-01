# Generated by Django 2.0.1 on 2018-01-31 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180122_0810'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updateDate', models.DateField(default='2018-1-20')),
                ('savePrice', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('currentPrice', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='categories.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagePath',
            field=models.ImageField(default='No_imange_yet', upload_to=''),
        ),
    ]
