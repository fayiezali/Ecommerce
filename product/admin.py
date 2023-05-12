from django.contrib import admin
from .models import * # import all models
from django.utils.html import format_html
#
#
#
# Add The Child Table(ProductImageMODEL) Inside The Parent Table(ProductMODEL) 
class ProductImageMODELAdmin(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = ProductImageMODEL
#
#
#
# The class has been inherited as an addict in order to make a modification / customization 
class ProductMODELAdmin(admin.ModelAdmin):
	# Admin View for Product Model
	# The fields to be shown on the Admin page
	list_display         = ('picture_displayDEF','product_name','product_available','product_description','product_original_price','product_selling_price','product_offer_price','product_stock_quantity','product_created','product_updated','product_image',)
	list_filter           = ('product_available','product_name','product_original_price','product_selling_price','product_offer_price','product_stock_quantity',) # filter by Available Field
	list_editable         = ('product_name','product_available','product_description','product_original_price','product_selling_price','product_stock_quantity',)
	prepopulated_fields   = {'product_slug':('product_name',)} # Auto Filled # Autofill Slug field from name field  
	empty_value_display  = '-empty-'
	inlines = [ProductImageMODELAdmin]
	# list_display_links = ('CATE_category_image',) 

	# View The Image On the Admin Page
	def picture_displayDEF(self,obj):
	        return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.product_image.url))
	picture_displayDEF.short_description='Picture' 
#
# Display the Model on the Admin Page
admin.site.register(ProductMODEL, ProductMODELAdmin) 
#
#
#
# Admin View for Product Image Model
class ProductImageMODELAdmin(admin.ModelAdmin):
	# The fields to be shown on the Admin page
	list_display        = ('picture_displayDEF','ProductImage_product','ProductImage_image',)

	# View The Image On the Admin Page
	def picture_displayDEF(self,obj):
	        return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.Cate_category_image.url))
	picture_displayDEF.short_description='Picture' 
#
# Display the Model on the Admin Page
admin.site.register(ProductImageMODEL, ProductImageMODELAdmin) 
#
#

