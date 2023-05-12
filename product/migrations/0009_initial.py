# Generated by Django 4.1.3 on 2023-02-25 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0021_initial'),
        ('product', '0008_alter_productmodel_index_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMODEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(db_index=True, max_length=200, verbose_name='Name')),
                ('product_slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug')),
                ('product_image', models.ImageField(db_index=True, default='Default_Image.png', upload_to='Productes_File_Photo/', verbose_name='Image Preview')),
                ('product_description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('product_original_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Original Price')),
                ('product_selling_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Selling Price')),
                ('product_offer_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Offer Price')),
                ('product_stock_quantity', models.IntegerField(verbose_name='Stock Quantity')),
                ('product_available', models.BooleanField(default=True, verbose_name='Available')),
                ('product_created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('product_updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='category.categorymodel', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('-product_created',),
                'index_together': {('id', 'product_slug')},
            },
        ),
        migrations.CreateModel(
            name='ProductImageMODEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductImage_image', models.ImageField(db_index=True, default='Default_Image.png', upload_to='Productes_File_Photo/', verbose_name='Image Preview')),
                ('ProductImage_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='product.productmodel', verbose_name='Product Name')),
            ],
            options={
                'verbose_name': 'Product Image',
                'verbose_name_plural': 'Products Images',
                'ordering': ('-ProductImage_product',),
                'index_together': {('id',)},
            },
        ),
    ]