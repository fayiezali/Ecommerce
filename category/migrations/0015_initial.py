# Generated by Django 4.1.3 on 2023-02-19 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0014_remove_categorysubmodel_csub_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMODEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATE_name', models.CharField(db_index=True, max_length=200, verbose_name='Name')),
                ('CATE_slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
                ('CATE_category_image', models.ImageField(db_index=True, default='Default_Image.png', upload_to='Catgory_File_Photo/', verbose_name='Image Preview')),
                ('CATE_available', models.BooleanField(db_index=True, default=True, verbose_name='Available')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('CATE_name',),
            },
        ),
    ]