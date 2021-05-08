from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/<str:pk>/', views.user, name='user'),
    path('edit/', views.edit, name='edit'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]