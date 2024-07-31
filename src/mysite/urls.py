"""
URL configuration for mysite project.

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
from django.contrib import admin, auth
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Vulnerability: A05:2021-Security Misconfiguration
    # The admin url in configured insecurely
    # This causes that it's much easier to make bruteforce attacks as the admin panel is not hidden in any way
    # Fix is to change the line something like this: path('adminsecret838383/', admin.site.urls)

    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='pages/login.html', next_page='/cellar')),
    path('logout/', LogoutView.as_view(next_page='/')),
    path('', include('pages.urls')),
    path("cellar/", include("cellar.urls"))
,]
