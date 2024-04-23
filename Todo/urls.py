"""
URL configuration for Todo project.

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
from myapp.views import Register,Signin,Add_task,Delete,Update,Signout,Delete_acc,Profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',Register.as_view(),name='register'),
    path('login/',Signin.as_view(),name='login'),
    path('',Add_task.as_view(),name='index'),
    path('delete/<int:key>',Delete.as_view(),name='delete'),
    path('update/<int:key>',Update.as_view(),name='update'),
    path('logout/',Signout.as_view(),name='logout'),
    path('delete_acc/',Delete_acc.as_view(),name='delete_acc'),
    path('profile/',Profile.as_view(),name='profile'),
]
