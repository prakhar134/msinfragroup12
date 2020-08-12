
from django.urls import path
from .import views
urlpatterns = [
    path('', views.loginpage, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register', views.Register, name='register'),
]
