# Generated by Django 4.1.3 on 2023-02-19 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0013_alter_categorymodel_cate_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorysubmodel',
            name='CSUB_category',
        ),
        migrations.DeleteModel(
            name='CategoryMODEL',
        ),
        migrations.DeleteModel(
            name='CategorySubMODEL',
        ),
    ]
