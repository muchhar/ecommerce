"""myproject URL Configuration

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
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$',views.index,name="home"),
    url(r'^login$',views.loginu,name="login"),
    url(r'^signup$',views.signupu,name="signup"),
    url(r'^otp$',views.otpu,name="otp"),
    url(r'^cartpage$',views.cartpage,name="cartpage"),
    url(r'^sendagain$',views.sendagain1,name="otpagain"),
    url(r'^forgotpass$',views.forg,name="forgotpass"),
    url(r'^setpassword$',views.setpass,name="setpass"),
    url(r'^logout$',views.logout,name="Logout"),
    url(r'^conadd$',views.conadd,name="conadd"),
    url(r'^comment/$',views.comment,name='comment'),
    url(r'^rate/$',views.rate,name='rate'),
    url(r'^youracc/$',views.youracc,name='youracc'),
    url(r'^changepass/$',views.changepass,name='changepass'),
    url(r'^yourorder/$',views.yourorder,name='yourorder'),
    #url(r'^productv(?P<id>\d+)$',views.productv,name="produtview"),
    url(r'^productv/(?P<ped>\d+)$',views.productv,name='productv'),

    url(r'^upimg/(?P<mai>\d+)/(?P<mai2>\d+)$',views.upimg,name='upimg'),
    url(r'^addtocart/(?P<ped>\d+)$',views.addtocart,name='addtocart'),

    url(r'^remove/(?P<pid>\d+)$',views.remove,name='remove'),
    url(r'^cancel/(?P<pid>\d+)$',views.cancel,name='cancel'),

   # url(r'^admin/$',auth_views.login,{'template_name':'adminsite/login.html'},name='login'),
    ##url( r'^admin/$',auth_views.LoginView.as_view(template_name="adminsite/login.html"), name="login"),
    ##url( r'^adminlogout/$',auth_views.LogoutView.as_view(template_name="adminsite/logout.html"), name="logout"),
    ##url(r'^addproduct$',views.addproduct,name="addproduct"),
	#url(r'^logout/$',auth_views.logout,{'template_name':'adminsite/addproduct.html'},name='logout'),


]
