# Generated by Django 4.1.3 on 2023-02-22 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0018_alter_subcategorymodel_subcat_category_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'ordering': ('Cate_name',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='subcategorymodel',
            options={'ordering': ('SubCat_name',), 'verbose_name': 'Sub Category', 'verbose_name_plural': 'Sub Categories'},
        ),
    ]
