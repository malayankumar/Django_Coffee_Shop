# Generated by Django 5.1.7 on 2025-03-11 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic',
            field=models.ImageField(upload_to='products/', verbose_name='Product Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Price (₹)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=1, verbose_name='Stock Quantity'),
        ),
    ]
