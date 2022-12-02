from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout 

def login_DEF(request): # 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request,('Youre logged in'))
                return redirect('dashboard-URL')
                # return render(request, "dashboard/dashboard.html", {'})
            else:
                messages.success(request,('ACCOUNT NOT ACTIVE'))
                return redirect('login-URL')
        else:
            messages.add_message(request, messages.ERROR, u'إسم المستخدم او كلمة المرور غير صحيحة')
            return render(request, 'login_logout/login.html', {})
    else:
        return render(request, 'login_logout/login.html', {})


def logout_confirm_DEF(request):
    return render(request , 'login_logout/logout_confirm.html', {}) 


def logout_done_DEF(request):
    logout(request)
    return render(request , 'login_logout/logout_done.html', {})


def login_page_DEF(request):
    return render(request,'login_logout/login.html', {})
#############################
# from django.shortcuts import render
# from django.views.generic import TemplateView
#
#
# # Create your views here.
# # Logout Confirm From App
# class LogoutConfirmClass(TemplateView):
#     pass
# #
# # Logout Done From App
# class LogoutDoneClass(TemplateView):
#     pass

# from django.shortcuts import render , redirect
# from django.contrib import messages
# from django.contrib.auth import login, authenticate, logout 
# def user_login(request): # 16
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username = username, password = password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 messages.success(request,('Youre logged in'))
#                 # fname = user.first_name
#                 # return render(request, "dashboard/dashboard.html", {'fname': fname})
#                 return redirect('dashboard-URL')
#             else:
#                 messages.success(request,('ACCOUNT NOT ACTIVE'))
#                 return redirect('user-login-URL')
#                 # return redirect('/')
#                 # return HttpResponse("ACCOUNT NOT ACTIVE")
#         else:
#             messages.add_message(request, messages.ERROR, u'إسم المستخدم او كلمة المرور غير صحيحة')
#             return render(request, 'login_logout/user_login.html', {})
#     else:
#         return render(request, 'login_logout/user_login.html', {})
