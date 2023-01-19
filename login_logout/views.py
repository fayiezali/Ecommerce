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



# def login_DEF(request): # 
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username = username, password = password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 messages.success(request,('Youre logged in'))
#                 return redirect('dashboard-URL')
#                 # return render(request, "dashboard/dashboard.html", {'})
#             else:
#                 messages.success(request,('ACCOUNT NOT ACTIVE'))
#                 return redirect('login-URL')
#         else:
#             messages.add_message(request, messages.ERROR, u'إسم المستخدم او كلمة المرور غير صحيحة')
#             return render(request, 'login_logout/login.html', {})
#     else:
#         return render(request, 'login_logout/login.html', {})
