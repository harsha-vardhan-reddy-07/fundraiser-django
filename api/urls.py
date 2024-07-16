from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('login/', views.login),
    path('register/', views.register),

    path('load-home/', views.loadHome),
    path('home/<str:id>', views.home),

    path('load-newfundraiser/', views.loadNewFundraiser),
    path('newfundraiser/<str:id>', views.newFundraiser),

    path('load-myfundraisers/', views.loadMyFundraisers),
    path('myfundraisers/<str:id>', views.myFundraisers),

    path('updatefundraiser/<str:id>/', views.updateFundraiser),
    path('fundraiser/<str:donarId>/<str:fundId>/', views.fundraiser),
     
    path('admin/', views.admin),
    path('allusers/', views.allUsers),
    path('allfundraisers/', views.allFundraisers),
    path('admin-fundraiser/<str:id>/', views.adminFundraiser),
    path('alldonations/', views.allDonations),
]

