from django.urls import path
from . import views


urlpatterns = [
	path('api/register/', views.registerPage, name="register"),
	path('api/login/', views.loginPage, name="login"),  
	path('api/logout/', views.logoutUser, name="logout"),
]