# Generated by Django 5.2.4 on 2025-07-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=0),
        ),
    ]
