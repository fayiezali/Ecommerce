# Generated by Django 4.1.3 on 2023-02-25 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0021_initial'),
        ('product', '0010_alter_productmodel_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='category.subcategorybranchmodel', verbose_name='Sub Category Branch'),
        ),
    ]
