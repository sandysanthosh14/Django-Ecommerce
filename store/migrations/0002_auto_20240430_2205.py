# Generated by Django 3.2 on 2024-05-01 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='protects',
            new_name='products',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='prize',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='protect_name',
            new_name='product_name',
        ),
    ]
