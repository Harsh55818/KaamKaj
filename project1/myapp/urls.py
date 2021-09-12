from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('companysignup/', views.companysignup, name='companysignup'),
    path('companylogin/', views.companylogin, name='companylogin'),
    path('company/<cname>/', views.company, name='company'),
    path('company/<cname>/profile/', views.companyprofile, name='companyprofile'),
    path('poster/', views.poster, name='poster'),
    path('internsignup/', views.internsignup, name='internsignup'),
    path('internlogin/', views.internlogin, name='internlogin'),
    path('intern/<iname>/', views.intern, name='intern'),
    path('intern/<iname>/profile/', views.internprofile, name='internprofile'),
]