from django.shortcuts import render , redirect

import random

from django.contrib.auth import login, authenticate ,logout

from django.contrib import messages

from django.contrib.auth.models import User # إستيراد اسم المستخدم

from . models import otp_MODEL
#
#
#
# Display Authorization Web Page
def authorization_DEF(request):
    return render(request,'otp/authorization.html', {})
#
#
def authorization_with_otp_DEF(request): # 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user:
                if user.is_active:
                    login(request, user)
                    messages.success(request,('User Is Active'))
                    return redirect('authorization-URL')
                else:
                    messages.success(request,('User Is Not Active'))
                    return redirect('login_page-URL')
        else:
            messages.success(request,('User Name or Password Is Incorrect'))
            return redirect('login_page-URL')
    else:
        return redirect('login_page-URL')
#
#
# Check the password for one time
def login_with_otp_DEF(request): # 
    if request.method == 'POST':
    # Verify that the name is not used by another user
        one_time_password_current= request.POST.get('txt_one_time_password_current')
        if otp_MODEL.objects.filter(otp_one_time_password=one_time_password_current).exists():
            messages.success(request,('Youre logged in'))
            return redirect('dashboard-URL')
        else:
            logout(request)
            messages.success(request,('The One Time Password is Incorrect'))
            return redirect('login_page-URL')
    else:
        messages.success(request,('No POST method'))
        return redirect('login_page-URL')



def number_random_DEF(request):
    ndnumber_random = random.random()
    ndnumber_random = random.randrange(1000, 10000)
    otp_one_time_password=ndnumber_random
    context={'otp_one_time_password': otp_one_time_password}
    return render(request, "otp/authorization.html" , context)

def get_number_random_otp():
    ndnumber_random = random.random()
    ndnumber_random = random.randrange(1000, 10000)
    otp_one_time_password=ndnumber_random
    context={'otp_one_time_password': otp_one_time_password}
    return otp_one_time_password





# def login_with_otp_DEF(request): # 
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username = username, password = password)
#         if user:
#                 if user.is_active:
#                     return redirect('authorization-URL')
#         else:
#             print('error')
#             messages.add_message(request, messages.ERROR, u'إسم المستخدم او كلمة المرور غير صحيحة')
#             return render(request, 'login_logout/login.html', {})
#     else:
#         return render(request, 'login_logout/login.html', {})




                # if  user.is_active:
                #     login(request, user)
                #     return redirect('authorization-URL')
                # if not user.is_active:
                #     messages.success(request,('Not Active'))
                #     return redirect('login-URL')
                # verification_code =1234
                # otp_otp =1234
                # if verification_code == otp_otp:
                #     login(request, user)
                #     messages.success(request,('Youre logged in'))
                #     return redirect('dashboard-URL')




            #  print(user)
            #  if  not user.is_active:
            #      messages.ERROR(request,('Not Active'))
            #      return redirect('login-URL')
            # if  user.is_active:
            #     login(request, user)
            #     return redirect('authorization-URL')
            # verification_code =1234
            # otp_otp =1234
            # if verification_code == otp_otp:
            #     messages.success(request,('Youre logged in'))
            #     return redirect('dashboard-URL')
            # else:
            #     verification_code != otp_otp
            #     messages.ERROR(request,('OTP is Not incorrect'))
            #     return redirect('authorization-URL')
