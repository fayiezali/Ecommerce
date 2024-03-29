"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #
        # App1 .........
    path('', include('dashboard.urls')),
    #
    # App2 .........
    path('', include('login_logout.urls')),
    #
    # App3 dashboard
    path('', include('password_change.urls')),
    #
    # App4 login_logout
    path('', include('password_reset.urls')),
    #
    # App5 login_logout
    path('', include('register.urls')),
    #
    path('', include('otp.urls')), 
    #
    path('', include('whatsapp.urls')),
    #
    path('', include('forgot_password.urls')),
    #
    path('', include('messages_alert.urls')),   
    #
    path('', include('store.urls')),

        # path('', include('product.urls')),    

    # path("accounts/", include("django.contrib.auth.urls")),  # new
]
#
#
#
# Defines Folder "static" & "media" Files So that The Project Can Access Them
if settings.DEBUG is True:
    # Folder "static" Files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Folder media" Files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)