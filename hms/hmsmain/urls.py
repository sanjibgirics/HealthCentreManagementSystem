"""hmsmain URL Configuration

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
from django.urls import path,include
from . import views
from django.views.generic import TemplateView
app_name = 'hmsmain'
urlpatterns = [
    path('',views.index,name='hmsmain'),
    path('about/',views.about,name='about'),
    path('facilities/',views.facilities,name='facilities'),
    path('people/',views.people,name='people'),
    path('login/',views.login1,name='login'),
    path('logout1',views.logout1,name='logout'),
    path('login/loginHandle/',views.loginHandle,name='loginHandle'),
    path('addMedicine/',views.addMedicine,name='addMedicine'),
    path('addMedicineHandle/',views.addMedicineHandle,name='addMedicineHandle'),
    path('raiseOrder/', views.raiseOrder, name='raiseOrder'),
    path('raiseOrderHandle/', views.raiseOrderHandle, name='raiseOrderHandle'),
    path('viewMedicine/',views.viewMedicine,name='viewMedicine'),
    path('viewPendingOrders/', views.viewPendingOrders, name='viewPendingOrders'),
    path('forwardOrder/', views.forwardOrder, name='forwardOrder'),
    path('revertOrder/', views.revertOrder, name='revertOrder'),
    path('userHome/', views.userHome, name='userHome'),
    path('viewOrders/',views.viewOrders,name='viewOrders'),
    path('issueMedicine/', views.issueMedicine, name='issueMedicine'),
    path('issueMedicineHandle/', views.issueMedicineHandle, name='issueMedicineHandle'),
    path('viewConsumption/',views.viewConsumption,name='viewConsumption'),
    path('editOrderPage/', views.editOrderPage, name='editOrderPage'),
    path('editOrder/', views.editOrder, name='editOrder'),
]
