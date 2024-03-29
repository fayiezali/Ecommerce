# Generated by Django 4.1.3 on 2023-02-17 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'ordering': ('CATE_name',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='categorysubmodel',
            options={'ordering': ('CSUB_name',), 'verbose_name_plural': 'Sub Categories'},
        ),
        migrations.RenameField(
            model_name='categorymodel',
            old_name='cate_available',
            new_name='CATE_available',
        ),
        migrations.RenameField(
            model_name='categorymodel',
            old_name='cate_category_image',
            new_name='CATE_category_image',
        ),
        migrations.RenameField(
            model_name='categorymodel',
            old_name='cate_name',
            new_name='CATE_name',
        ),
        migrations.RenameField(
            model_name='categorymodel',
            old_name='cate_slug',
            new_name='CATE_slug',
        ),
        migrations.RenameField(
            model_name='categorysubmodel',
            old_name='csub_available',
            new_name='CSUB_available',
        ),
        migrations.RenameField(
            model_name='categorysubmodel',
            old_name='csub_category_image',
            new_name='CSUB_category_image',
        ),
        migrations.RenameField(
            model_name='categorysubmodel',
            old_name='csub_name',
            new_name='CSUB_name',
        ),
        migrations.RenameField(
            model_name='categorysubmodel',
            old_name='csub_slug',
            new_name='CSUB_slug',
        ),
        migrations.RemoveField(
            model_name='categorysubmodel',
            name='csub_category',
        ),
        migrations.AddField(
            model_name='categorysubmodel',
            name='CSUB_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categories_sub', to='category.categorymodel', verbose_name='Category'),
            preserve_default=False,
        ),
    ]
