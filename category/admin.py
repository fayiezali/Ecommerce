from django.contrib import admin
from .models import *
from django.utils.html import format_html
#
#
#
class CategoryMODELAdmin(admin.ModelAdmin):
	'''
		Admin View for Category Model
	'''
	# The fields to be shown on the Admin page
	list_display        = ('picture_displayDEF','Cate_name','Cate_available','Cate_category_image',)
	list_filter          = ('Cate_available','Cate_name',) # filter by Available Field
	list_editable        = ('Cate_name','Cate_available',)
	prepopulated_fields  = {'Cate_slug':('Cate_name',)} # Auto Filled # Autofill Slug field from name field  
	empty_value_display = '-empty-'
	# list_display_links = ('CATE_category_image',) 

	# View The Image On the Admin Page
	def picture_displayDEF(self,obj):
	        return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.Cate_category_image.url))
	picture_displayDEF.short_description='Picture' 
#
#
#
class SubCategoryMODELAdmin(admin.ModelAdmin):
	'''
		Admin View for Category Sub Model
	'''
	# The fields to be shown on the Admin page
	list_display        = ('picture_displayDEF','SubCat_name','SubCat_available','SubCat_category_image',)
	list_filter          = ('SubCat_available','SubCat_name',) # filter by Available Field
	list_editable        = ('SubCat_name','SubCat_available',)
	prepopulated_fields  = {'SubCat_slug':('SubCat_name',)} # Auto Filled # Autofill Slug field from name field  
	empty_value_display = '-empty-'
	# list_display_links = ('CATE_category_image',) 

	# View The Image On the Admin Page
	def picture_displayDEF(self,obj):
	        return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.SubCat_category_image.url))
	picture_displayDEF.short_description='Picture' 
#
#
# Display the Model on the Admin Page
admin.site.register(CategoryMODEL, CategoryMODELAdmin)
admin.site.register(SubCategoryMODEL, SubCategoryMODELAdmin)







# class ProductAdmin(admin.ModelAdmin):
# 	'''
# 		Admin View for Product
# 	'''
# 	list_display = ('name','slug','category','price','stock','available','created','updated',)
# 	list_filter = ('available','created','updated','category',)
# 	list_editable = ('price','stock','available',)
# 	prepopulated_fields = {'slug':('name',)}

# admin.site.register(Product, ProductAdmin)


