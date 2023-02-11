from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout 



# Display Login Web Page
def login_page_DEF(request):
    return render(request,'login_logout/login.html', {})


# Logout Confirme
def logout_confirm_DEF(request):
    return render(request , 'login_logout/logout_confirm.html', {}) 


# Checkout Confirmed Successfull
def logout_done_DEF(request):
    logout(request)
    return render(request , 'login_logout/logout_done.html', {})
