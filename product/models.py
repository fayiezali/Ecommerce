# from django.db import models
# from django.urls import reverse
# from category.models import CategoryMODEL , CategorySubMODEL


# # class ProductImage(BaseModel):
# #     product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="product_images")
# #     image =  models.ImageField(upload_to="product")
    
    
    
# class ProductMODEL(models.Model):

# 	pro_category    = models.ForeignKey(CategorySubMODEL,related_name='product',on_delete=models.CASCADE)
# 	pro_name      = models.CharField(max_length=200 , db_index=True)
# 	pro_slug 	   = models.SlugField(max_length=200 , db_index=True)
# 	pro_image 	  = models.ImageField(blank=True)
# 	pro_description = models.TextField(blank=True)
# 	pro_price 	   = models.DecimalField(max_digits=10 , decimal_places=2)
# 	pro_stock 	   = models.PositiveIntegerField()
# 	pro_available 	= models.BooleanField(default=True)
# 	pro_created    = models.DateTimeField(auto_now_add=True)
# 	pro_updated   = models.DateTimeField(auto_now=True)

# 	class Meta:
# 		ordering = ('-pro_created',)
# 		index_together = (('id','pro_slug'),)
# 		verbose_name = "Product"
# 		verbose_name_plural = "Products"

# 	def __str__(self):
# 		return self.pro_name

# 	def get_absolute_url(self):
# 		return reverse('product:product_detail',args=[self.id,self.pro_slug])