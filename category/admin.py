from django.contrib import admin
from .models import CategoryMODEL , CategorySubMODEL


class CategoryMODELAdmin(admin.ModelAdmin):
	'''
		Admin View for Category
	'''
	list_display = ('c_name','c_slug',)
	prepopulated_fields = {'c_slug':('c_name',)}
#
#
class CategorySubMODELAdmin(admin.ModelAdmin):
	'''
		Admin View for Category Sub
	'''
	list_display = ('cs_name','cs_slug',)
	prepopulated_fields = {'cs_slug':('cs_name',)}
#
#
admin.site.register(CategoryMODEL, CategoryMODELAdmin)
admin.site.register(CategorySubMODEL, CategorySubMODELAdmin)



# class ProductAdmin(admin.ModelAdmin):
# 	'''
# 		Admin View for Product
# 	'''
# 	list_display = ('name','slug','category','price','stock','available','created','updated',)
# 	list_filter = ('available','created','updated','category',)
# 	list_editable = ('price','stock','available',)
# 	prepopulated_fields = {'slug':('name',)}

# admin.site.register(Product, ProductAdmin)




