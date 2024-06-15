"""
URL configuration for stacks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from home.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from accounts.views import *
from django.contrib.auth.views import LoginView
from booking.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('register/', register,name="register"),
    # path('login/',coustomlogin, name='login'),
    path('login/accounts/profile/', profile, name='profile'),
    path('add_question/', add_question, name='add_question'),
    # path('login/',coustomlogin, name='login'),
    path('login/accounts/profile/', profile, name='profile'),
    path('login/accounts/profile/', profile, name='profile'),
    path('profile/', profile, name='profile'),
    path('user_page/', user_page, name='user_page'),
    path('add_question/', add_question, name='add_question'),
    path('login/index.html',home,name="home"),
    path('combined/new/', combined_create_view, name='combined_create'),
    path('success/', success_view, name='success_page'),  
    path('display/', display_cards_view, name='display_cards'),
    path('profile/combined/new/',combined_create_view , name='combine'),
    path('book/', book,name="book"),
    path('explore/',explore,name="explore"),
    path('save-booking/', save_booking, name='save_booking'),
    path('profile/',profile, name='profile'),
    path('user_page/', user_page, name='user_page'),
    path('register/', register, name='register'),
    path('login/', customlogin, name='login'),
    path('logout/',logout_view, name='logout'),
   path('explore/index',home,name="home"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)