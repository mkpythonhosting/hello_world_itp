# menu/urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.homemenu, name = 'home_page'),
    path('login/', views.loginmenu, name = 'login_page'),
    path('about/', views.aboutmenu, name = 'about_page'),
    path('login/register/',views.registermenu, name = 'register_page'),
]