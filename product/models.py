from django.db import models
from django.urls import reverse
from category.models import CategoryMODEL 
from .models import *



# Model Proudect
class ProductMODEL(models.Model):
    product_category     = models.ForeignKey(CategoryMODEL , related_name='products', on_delete=models.CASCADE ,  verbose_name='Product')
    product_name        = models.CharField(max_length=200 , db_index=True , verbose_name='Name')
    product_slug         = models.SlugField(unique=True  , null=True , blank=True , verbose_name='Slug')
    product_image        = models.ImageField(upload_to="Productes_File_Photo/" , db_index=True , blank=False  , null=False , verbose_name="Image Preview"  , default='Default_Image.png')
    product_description    = models.TextField(null=True , blank=True , verbose_name='Description')
    product_original_price  = models.DecimalField(max_digits=10,decimal_places=2 , verbose_name='Original Price')
    product_selling_price   = models.DecimalField(max_digits=10,decimal_places=2 , verbose_name='Selling Price')
    product_stock_quantity  = models.IntegerField(verbose_name='Stock Quantity') 
    product_available 	   = models.BooleanField(default=True , verbose_name='Available')
    product_created 	  = models.DateTimeField(auto_now_add=True , verbose_name='Created')
    product_updated 	  = models.DateTimeField(auto_now=True , verbose_name='Updated')

    class Meta:
        ordering = ('-product_created',)
        index_together = (('id','product_slug'),)
        verbose_name = "Product"
        verbose_name_plural = "Products"

    # 'admin'display the field name on a page
    def __str__(self):
        return self.product_name

    # def get_absolute_url(self):
    #     return reverse('product:product_detail',args=[self.id,self.product_slug])



class ProductImageMODEL(models.Model): 
    ProductImage_product = models.ForeignKey(ProductMODEL ,  related_name="product_images" ,on_delete=models.CASCADE ,  verbose_name='Product Name')
    ProductImage_image   = models.ImageField(upload_to="Productes_File_Photo/" , db_index=True , blank=False  , null=False , verbose_name="Image Preview"  , default='Default_Image.png')

    class Meta:
        ordering = ('-ProductImage_product',)
        index_together = (('id',),)
        verbose_name = "Product Image"
        verbose_name_plural = "Products Images"

    # 'admin'display the field name on a page 
    def __str__(self):
        return self.ProductImage_product

    # def get_absolute_url(self):
    #     return reverse('product:product_detail',args=[self.id])
