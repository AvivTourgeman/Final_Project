# Generated by Django 3.2.6 on 2022-11-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_rename_category_id_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
