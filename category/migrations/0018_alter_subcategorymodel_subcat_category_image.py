# Generated by Django 4.1.3 on 2023-02-19 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0017_subcategorymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategorymodel',
            name='SubCat_category_image',
            field=models.ImageField(db_index=True, default='Default_Image.png', upload_to='Sub_Catgories_File_Photo/', verbose_name='Image Preview'),
        ),
    ]