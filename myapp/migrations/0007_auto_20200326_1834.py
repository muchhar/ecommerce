# Generated by Django 3.0.3 on 2020-03-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20200326_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pp1',
            field=models.ImageField(null=True, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pp2',
            field=models.ImageField(null=True, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pp3',
            field=models.ImageField(null=True, upload_to='gallery'),
        ),
    ]
