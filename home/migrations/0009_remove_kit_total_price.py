# Generated by Django 4.2.9 on 2024-04-30 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_kit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kit',
            name='total_price',
        ),
    ]
