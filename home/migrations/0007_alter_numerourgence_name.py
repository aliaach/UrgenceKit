# Generated by Django 4.2.9 on 2024-04-30 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_stock_name_remove_stock_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numerourgence',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]