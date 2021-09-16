from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('contact/', views.contact),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('SLP/',views.sSLP, name="SLP" )
]
