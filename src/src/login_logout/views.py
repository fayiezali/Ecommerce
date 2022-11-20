from django.shortcuts import render , redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
# from django.urls import reverse
# from django.contrib.auth import login, authenticate, logout 
#
# Logout Confirm From App
class LogoutConfirmClass(TemplateView):
    template_name = 'registration/logout_confirm.html' # The Page HTML to Display
#
# Logout Done From App
class LogoutDoneClass(TemplateView):
    template_name = 'registration/logout_done.html' # The Page HTML to Display
#
# 
# #
# def user_login(request): # 16
#     if request.method == 'POST':
#         # username = request.POST['username']
#         Email = request.POST['email']
#         password = request.POST['password']
#         # user = authenticate(request, username = username, password = password)
#         user = authenticate(request, email = Email, password = password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 messages.success(request,('Youre logged in'))
#                 fname = user.first_name
#                 return render(request, "dashboard/dashboard.html", {'fname': fname})
#                 # return redirect('/')
#                 # return HttpResponseRedirect(reverse('index'))
#             else:
#                 messages.success(request,('ACCOUNT NOT ACTIVE'))
#                 return redirect('/')
#                 # return HttpResponse("ACCOUNT NOT ACTIVE")
#         else:
#             messages.add_message(request, messages.ERROR, u'Введены неправильные имя пользователя и пароль')
#             return render(request, 'login_logout/user_login.html', {})
#     else:
#         return render(request, 'login_logout/user_login.html', {})
# ###########################################################
# def user_logout(request):
#     logout(request)
#     return redirect('/')
#
#
# def user_login(request):
#     # Put the data to be displayed on the page in context
#     context={}
#     return render(request,'login_logout/user_login.html', context)

#######################################
# def loginCredentials(request): # 14
#     if request.method == 'POST':
#         Email = request.POST['email']
#         Password = request.POST['password']
#         try: 
#             user = authentication.sign_in_with_email_and_password(Email, Password)
#             # inform = authentication.get_account_info(user['idToken'])
#             # print(inform)
#             request.session['idToken'] = str(user['idToken'])
#             messages.success(request,"User Successfully SignIn")
#             return render(request,'pages/welcome.html')
#         except:
#             messages.error(request,"Invallid Credentials")
#             return redirect('/')
#     else:
#         return HttpResponse("404 not found")
###########################################################
# def loginUser(request): # 11
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # check if user  has entered correct credentials
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("/")
#         else:
#             return render(request, 'login.html')
#     return render(request, 'login.html')
###########################################################
# def login(request): # 13
# 	if request.method == 'POST':
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = auth.authenticate(username=username,password=password)
# 		if user is not None:
# 			auth.login(request,user)
# 			return redirect('/')
# 		else:
# 			messages.info(request,'invalid credentials')
# 			return redirect('login')
# 	else:
# 		return render(request,'login.html')
###########################################################
# def signin(request):# 13
#     if request.method == "POST":
#         username = request.POST['Username']
#         pass1 = request.POST['pass1']
#         user = authenticate(username=username, password=pass1)
#         if user is not None:
#             login(request,user)
#             fname = user.first_name
#             return render(request, "authentication/index.html", {'fname': fname})
#         else:
#             messages.error(request, "Incorrect Credentials!")
#             return redirect('home')
#     return render(request,"authentication/signin.html")
###########################################################
# def login(request): # 14
#     if request.method == 'POST':
#         # Login User
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             messages.success(request, 'You are now logged in.')
#             return redirect('dashboard')
#         else:
#             messages.error(request, 'Invalid Account.')
#             return redirect('register')
#     else:
#         return render(request, 'accounts/login.html')
######################################################

# def login_user(request): # 14
# 	if request.method =='POST':
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(request, username=username, password=password)
# 		if user is not None:
# 			login(request, user)
# 			messages.success(request,('you have been logged in'))
# 			return redirect('home')
# 		else:
# 			messages.success(request,('Error login in log in with valid username..'))
# 			return redirect('login')
# 	else:
# 		return render(request,'login.html',{})
###########################################################
# def login_user (request): # 14
# 	if request.method == 'POST': #if someone fills out form , Post it 
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(request, username=username, password=password)
# 		if user is not None:# if user exist
# 			login(request, user)
# 			messages.success(request,('Youre logged in'))
# 			return redirect('home') #routes to 'home' on successful login  
# 		else:
# 			messages.success(request,('Error logging in'))
# 			return redirect('login') #re routes to login page upon unsucessful login
# 	else:
# 		return render(request, 'authenticate/login.html', {})
###########################################################
# def user_login(request): # 15
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(username=username, password=password)
#             if user:
#                 if user.is_active:
#                     login(request,user)
#                     return HttpResponseRedirect(reverse('index'))
#                 else:
#                     return HttpResponse("Account not Active!")
#             else:
#                 return HttpResponse("Invalid Login details Supplied!")
#         else:
#             return render(request, 'basicapp/login.html', {})
###########################################################
# def user_login(request): # 15
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username = username, password = password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 # redirect to a success page
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 return HttpResponse("ACCOUNT NOT ACTIVE")
#         else:
#             return HttpResponse('Invalid login details!')
#     else:
#         return render(request, 'myapp/login.html', {})
###########################################################
# def lgn(request): # 16
#     if request.method == 'POST':
#         username = request.POST.get('Username')
#         password =  request.POST.get('Password')
#         user = authenticate(username= username, password= password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 return HttpResponse('Not active')
#         else:
#             messages.add_message(request, messages.ERROR, u'Введены неправильные имя пользователя и пароль')
#             return render(request, 'login.html', {})
#     else:
#         return render(request, 'mapp/login.html')
###########################################################

# def user_login(request): # 16
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # Проверить сущетсвует ли такой пользователь в базе
#         user = authenticate(username=username, password=password)
#         if user:
#             # если существует и активен
#             if user.is_active:
#                 # Пропустить пользователя и дать ему сессию
#                 login(request, user)
#                 return HttpResponse('Вы авторизировались успешно!')
#             else:
#                 return HttpResponse('Ваш аккаунт - неактивен')
#         else:
#             # Сформировать сообщение для пользователя
#             messages.add_message(request, messages.ERROR, u'Введены неправильные имя пользователя и пароль')
#             return render(request, 'login.html', {})
#     else:
#         return render(request, 'login.html', {})
###########################################################
