"""web1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from old import views
urlpatterns = [
    path('',views.login),
    path('login',views.logins),
    path('index', views.index),
    path('register',views.register),
    path('regist',views.regist),
    # path('catch',views.catch),
    path('oldmanzhuce', views.oldmanzhuce),
    path('oldmanruzhu', views.oldmanruzhu),
    path('oldmanernv1', views.oldmanernv1),
    path('oldmanernv2', views.oldmanernv2),
    path('oldmanchuangjian', views.oldmanchuangjian),
    path('workmanzhuce', views.workmanzhuce),
    path('workmanruzhi', views.workmanruzhi),
    path('workmanchuangjian', views.workmanchuangjian),
    path('yigongzhuce', views.yigongzhuce),
    path('yigonggongzuo', views.yigonggongzuo),
    path('yigongchuangjian', views.yigongchuangjian),
    path('oldmanzhuce1', views.oldmanzhuce1),
    path('oldmanruzhu1', views.oldmanruzhu1),
    path('oldmanernv11', views.oldmanernv11),
    path('oldmanernv22', views.oldmanernv22),
    path('workmanzhuce1', views.workmanzhuce1),
    path('workmanruzhi1', views.workmanruzhi1),
    path('yigonggongzuo1', views.yigonggongzuo1),
    path('yigongzhuce1', views.yigongzhuce1),
    path('yigongchuangjian1', views.yigongchuangjian1),
    path('oldmanchuangjian1', views.oldmanchuangjian1),
    path('workmanchuangjian1', views.workmanchuangjian1),
    path('camera', views.camera),
    path('getface',views.getface),
    path('jiankong',views.jiankong),
    path('chart',views.chart),
    path('caiji',views.caiji),
    path('getface1',views.getface1),
]
