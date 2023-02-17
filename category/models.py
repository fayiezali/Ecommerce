from django.db import models
from django.urls import reverse
#
#
#
class CategoryMODEL(models.Model):
	
	c_name         = models.CharField(max_length=200 , db_index=True)
	c_slug          = models.SlugField(max_length=200 , db_index=True ,unique=True)
	c_category_image = models.ImageField(upload_to="catgories" ,  db_index=True , blank=True  , null=False ,)

	class Meta:
	    # 'Z-A' in descending order
		ordering = ('c_name',)
		# The Name of the Model That Will Be Displayed In The Admin Page
		verbose_name      = "Categories"
		verbose_name_plural = "Categories"

    # 'admin'display the field name on a page
	def __str__(self):
		return self.c_name

	# def get_absolute_url(self):
	# 	return reverse('shop:product_list_category',args=[self.slug])
	
	
class CategorySubMODEL(models.Model):
	
	cs_category      = models.ForeignKey(CategoryMODEL , related_name='categories_sub' , on_delete=models.CASCADE)
	cs_name         = models.CharField(max_length=200 , db_index=True)
	cs_slug          = models.SlugField(max_length=200 , db_index=True,unique=True)
	cs_category_image = models.ImageField(upload_to="catgories_sub" ,  db_index=True , blank=True  , null=False ,)

	class Meta:
	    # 'Z-A' in descending order
		ordering = ('cs_name',)
		# The Name of the Model That Will Be Displayed In The Admin Page
		verbose_name      = "Categories Sub"
		verbose_name_plural = "Categories Sub"

    # 'admin'display the field name on a page
	def __str__(self):
		return self.cs_name
