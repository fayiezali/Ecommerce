# Generated by Django 4.1.3 on 2023-02-18 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0009_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryimagemodel',
            name='CAIM_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category_image', to='category.categorymodel', verbose_name='Category Name'),
        ),
    ]
