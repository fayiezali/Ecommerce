from django.contrib import admin

from .models import *

class OtpMODELAdmin(admin.ModelAdmin):
	'''
		Admin View for Category
	'''
	list_display = ('otp_user','otp_one_time_password','otp_created_at',)

admin.site.register(otpMODEL , OtpMODELAdmin)
