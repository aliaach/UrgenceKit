# Generated by Django 4.2.9 on 2024-04-30 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_magazin_remove_product_info_product_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumeroUrgence',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='stock',
            name='number',
            field=models.CharField(default='', max_length=20),
        ),
    ]