from django.shortcuts import render , redirect

import random

from django.contrib.auth import login, authenticate ,logout

from django.contrib import messages

from django.contrib.auth.models import User # إستيراد اسم المستخدم

from . models import otp_MODEL

from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes 
from project import settings
# from . tokens import generate_token
import datetime
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
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
                if user.is_active:
                    login(request, user)
                    ##########################3
                    
                    number_random  = random.randrange(1000, 10000)
                    print('number_random:', number_random)
                    table_otp = otp_MODEL.objects.get(otp_user=user.id)
                    table_otp.otp_one_time_password = number_random
                    table_otp.save()
                    print('table_otp:' ,table_otp)
                    
                    # essages when account has been created in database
                    messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
                    
                    print('step(2) - The creation of the new user has been completed')
            
                    # Welcome Email
                    subject = "Welcome To Ecommerce Login!!"
                    # message = "Hello " + myuser.first_name + "!! \n" + "Welcome to our Space!! \nThank you for visiting our website.\n We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n$p@r$h\nCEO of nothing"        
                    message = "Hello " + user.first_name + "   \n" + "One Time Password"+ "\n" "Code:  " +  str(number_random) +  "\n" "Date/Time:  " + str(datetime.datetime.now()) + "\n\nThanking You\n$p@r$h\nCEO of nothing"        
                    # the email we will be using to send it to teh the new user
                    from_email = settings.EMAIL_HOST_USER
                    # the user email
                    to_list = [user.email]
                    # fail_silently is used for the purpose that if teh email is not send, teh app should not crash 
                    send_mail(subject, message, from_email, to_list, fail_silently=True)
                    print('step(3) - Welcome Send has been completed')
            
                
                
                #     # displaying messages when account has been created in database
                #     messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
                    
                #     print('step(2) - The creation of the new user has been completed')
            
                #     # Welcome Email
                #     subject = "Welcome to Django Login!!"
                #     message = "Hello " + myuser.first_name + "!! \n" + "Welcome to our Space!! \nThank you for visiting our website.\n We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n$p@r$h\nCEO of nothing"        
                #     # the email we will be using to send it to teh the new user
                #     from_email = settings.EMAIL_HOST_USER
                #     # the user email
                #     to_list = [myuser.email]
                #     # fail_silently is used for the purpose that if teh email is not send, teh app should not crash 
                #     send_mail(subject, message, from_email, to_list, fail_silently=True)
                #     print('step(3) - Welcome Send has been completed')
            
                #     # email for confiramtion of the account activation
                #     current_site = get_current_site(request)  # it will traget the diamin of teh current site
                #     email_subject = "Confirm your Email @ Authentication - Django Login!!"
                #     # the email_confirmation.html is the template to be used for every time confimation email is sent
                #     # ("email_confirmation.html", {dict})
                #     message2 = render_to_string('register/email_confirmation.html',{
                #         'name': myuser.first_name,
                #         'domain': current_site.domain,
                #         # getting user id
                #         'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
                #         # generating token with help of tokens.py
                #         'token': generate_token.make_token(myuser)
                #     })
                #     # creating an email object
                #     email = EmailMessage(
                #     email_subject,
                #     message2,
                #     # person sending the mail
                #     settings.EMAIL_HOST_USER,
                #     # person to whom the mail is to be send
                #     [myuser.email],
                #     )
                #     email.fail_silently = True
                #     email.send()
                #     print('step(4) - Send email for confiramtion of the account activation  has been completed')
            
                #     # now redirecting them to signin page
                #     return redirect('login-URL')
            
                # # return render(request, "register/register.html")
                    ###################################
                    messages.success(request,('User Is Active'))
                    messages.success(request,('otp_MODEL.save()'))
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
        one_time_password_current= request.POST['txt_one_time_password_current']

        # Verify the number of input letters
        if len(one_time_password_current) != 4:
            messages.error(request, "The One Time Password is Incorrect!")
            return redirect('authorization-URL')
        if not one_time_password_current.isnumeric():
            messages.error(request, "The Password Must Be One Time Numbers")
            return redirect('authorization-URL')
        
        # Check the passwords match
        # If  One Time Password Exists In Database
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



# def number_random_DEF(request):
#     ndnumber_random = random.random()
#     ndnumber_random = random.randrange(1000, 10000)
#     otp_one_time_password=ndnumber_random
#     context={'otp_one_time_password': otp_one_time_password}
#     return render(request, "otp/authorization.html" , context)

# def get_number_random_otp():
#     ndnumber_random = random.random()
#     ndnumber_random = random.randrange(1000, 10000)
#     otp_one_time_password=ndnumber_random
#     context={'otp_one_time_password': otp_one_time_password}
#     return otp_one_time_password





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
