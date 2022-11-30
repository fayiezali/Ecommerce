from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('signup', views.signup, name='signup-URL'),
    # path('signin', views.signin, name='signin'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path('signout', views.signout, name='signout'),
]







# from django.urls import path, include
# from register import views

# urlpatterns = [
#     path('signup/', views.signup, name="signup-URL"),
#     # path('login/', views.login, name="login"),
#     # path('verify/<token>', views.verify, name="verify"),
#     # path('profile/', views.profile, name="profile"),
#     # path('profile/changepassword', views.change_password, name="changepassword"),
#     # path('logout/', views.logout, name="logout"),
#     # path('forgetpassword/', views.forget_password, name="forgetpassword"),
#     # path('resetpassword/<token>', views.reset_password, name="resetpassword"),
# ]