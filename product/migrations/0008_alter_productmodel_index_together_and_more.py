# Generated by Django 4.1.3 on 2023-02-25 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_productimagemodel_productimage_product'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='productmodel',
            index_together=None,
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='product_category',
        ),
        migrations.DeleteModel(
            name='ProductImageMODEL',
        ),
        migrations.DeleteModel(
            name='ProductMODEL',
        ),
    ]
