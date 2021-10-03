from django.urls import path
from . import views


urlpatterns = [
	path('api/register/', views.registerPage, name="register"),
	path('api/login/', views.loginPage, name="login"),  
	path('api/logout/', views.logoutUser, name="logout"),
	path('api/user-account/', views.userPage, name="user-account"),
	path('api/account/', views.accountSettings, name="account"),
]