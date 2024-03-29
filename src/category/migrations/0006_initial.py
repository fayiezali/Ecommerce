# Generated by Django 4.1.3 on 2023-02-17 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0005_remove_categorysubmodel_cs_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMODEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_name', models.CharField(db_index=True, max_length=200, verbose_name='Name')),
                ('cate_slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
                ('cate_category_image', models.ImageField(blank=True, db_index=True, upload_to='catgories', verbose_name='Image')),
                ('cate_available', models.BooleanField(db_index=True, default=True, verbose_name='Available')),
            ],
            options={
                'verbose_name': 'Categories',
                'verbose_name_plural': 'Categories',
                'ordering': ('cate_name',),
            },
        ),
        migrations.CreateModel(
            name='CategorySubMODEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csub_name', models.CharField(db_index=True, max_length=200, verbose_name='Name')),
                ('csub_slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
                ('csub_category_image', models.ImageField(blank=True, db_index=True, upload_to='catgories_sub', verbose_name='Image')),
                ('csub_available', models.BooleanField(db_index=True, default=True, verbose_name='Available')),
                ('csub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories_sub', to='category.categorymodel')),
            ],
            options={
                'verbose_name': 'Sub Categories',
                'verbose_name_plural': 'Categories Sub',
                'ordering': ('csub_name',),
            },
        ),
    ]
