from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('login/', views.login),
    path('register/', views.register),
    path('home/', views.home),
    path('newfundraiser/', views.newFundraiser),
    path('myfundraisers/', views.myFundraisers),
    path('fundraiser/<int:id>/', views.fundraiser),
    path('updatefundraiser/<int:id>/', views.updateFundraiser),
    path('admin/', views.admin),
    path('allusers/', views.allUsers),
    path('allfundraisers/', views.allFundraisers),
    path('alldonations/', views.allDonations),
]

