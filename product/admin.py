# from django.contrib import admin
# from .models import ProductMODEL


# class ProductMODELAdmin(admin.ModelAdmin):
# 	'''
# 		Admin View for Product
# 	'''
# 	list_display = ('pro_name','pro_slug','pro_category','pro_price','pro_stock','pro_available','pro_created','pro_updated',)
# 	list_filter = ('pro_available','pro_created','pro_updated','pro_category',)
# 	list_editable = ('pro_price','pro_stock','pro_available',)
# 	prepopulated_fields = {'pro_slug':('pro_name',)}

# admin.site.register(ProductMODEL, ProductMODELAdmin)