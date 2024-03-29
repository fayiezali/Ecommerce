from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from project import settings
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes 
from . tokens import generate_token
# from django.utils.encoding import force_text
import django
from django.utils.encoding import force_str 
django.utils.encoding.force_text = force_str
import re
from django.contrib.auth.hashers import make_password, check_password

#
# validation formula
EMAIL_REGEX      = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
USERNAME_REGEX  = re.compile("[a-z0-9_]{3,15}")
FIRSTNAME_REGEX  = re.compile("[a-zA-Z]{2,20}")
LASTNAME_REGEX  = re.compile("[a-zA-Z]{2,20}")
PASSWARD_Criterian = {
                    "length_criteria":".{8,}",
                    "lowercase_criteria":"[a-z]+",
                    "uppercase_criteria":"[A-Z]+",
                    "number_criteria":"[0-9]+",
                    "symbol_criteria":"[^A-Za-z0-9]+",
                    }
#
#
def register_DEF(request):
    if request.method == 'POST':

        # take all field entered by user so we cam work with them on backend
        username = request.POST['username']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email    = request.POST['email']
        password = request.POST['pass1']
        pass2    = request.POST['pass2']

# defining some parameter for user to follow while making account
        #
        # Verify the validity of the inputs - UserName
        if not USERNAME_REGEX.match(username):
            messages.error(request, "User Name - The Entered Data Is incorrect")
            return redirect('register-URL')

        # Verify that the name is not used by another user
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('register-URL')

        # Verify the number of input letters
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('register-URL')

        # Verify the validity of the inputs - Email
        if not EMAIL_REGEX.match(email):
            messages.error(request, "EMAIL - The Entered Data Is incorrect")
            return redirect('register-URL')

        # Verify that the Email is not used by another user
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('register-URL')

        # Check the passwords match
        if password != pass2:
            messages.error(request, "Passwords didn't Matched!!")
            return redirect('register-URL')

################################################################
        # myuser=User()
        # myuser.username =request.POST['username']
        # myuser.first_name =request.POST['fname']
        # myuser.last_name =request.POST['lname']
        # myuser.email    =request.POST['email']
        # myuser.password =request.POST['pass1']
        # myuser.is_active  = False
        # hash_pswd      = make_password(myuser.password)
        # # Save the password
        # myuser.password = hash_pswd # Save the Password in the variable
        # myuser.save()        
################################################################        
        # creating user in database
        # create_user() takes from 2 to 4 positional arguments Only
        myuser = User.objects.create_user(username, password)
        myuser.email      = email
        myuser.first_name  = firstname
        myuser.last_name  = lastname 
        myuser.is_active   = False #account of user is not activated
        myuser.save()          # saving in database

        # displaying messages when account has been created in database
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

        # Welcome Email
        subject = "Welcome To Ecommerce Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to our Space!! \nThank you for visiting our website.\n We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n$p@r$h\nCEO of nothing"        
        # the email we will be using to send it to teh the new user
        from_email = settings.EMAIL_HOST_USER
        # the user email
        to_list = [myuser.email]
        # fail_silently is used for the purpose that if teh email is not send, teh app should not crash 
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # email for confiramtion of the account activation
        current_site = get_current_site(request)  # it will traget the diamin of teh current site
        email_subject = "Confirm your Email @ Authentication - Django Login!!"
        # the email_confirmation.html is the template to be used for every time confimation email is sent
        # ("email_confirmation.html", {dict})
        message2 = render_to_string('register/email_confirmation.html',{
            'name': myuser.first_name,
            'domain': current_site.domain,
            # getting user id
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            # generating token with help of tokens.py
            'token': generate_token.make_token(myuser)
        })
        # creating an email object
        email = EmailMessage(
        email_subject,
        message2,
        # person sending the mail
        settings.EMAIL_HOST_USER,
        # person to whom the mail is to be send
        [myuser.email],
        )
        email.fail_silently = True
        email.send()

        # now redirecting them to signin page
        return redirect('login_page-URL')

    return render(request, "register/register.html")



# for activating the account
def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        # fetching 
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('login_page-URL')
    else:
        messages.error(request, "Your Account activation failed!!")
        return redirect('register-URL')

