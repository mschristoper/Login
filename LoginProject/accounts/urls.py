from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('contact/', views.contact),
    path('login/', views.login),
    path('signup', views.signup, name='signup')
]
