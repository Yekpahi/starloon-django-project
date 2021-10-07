from django.urls import path
from . import views
from userAccount.views import ChangePasswordView


urlpatterns = [
	path('api/register/', views.registerPage, name="register"),
	path('api/login/', views.loginPage, name="login"),  
	path('api/logout/', views.logoutUser, name="logout"),
	path('api/profile/', views.profile, name='users-profile'),
	path('api/password-change/', ChangePasswordView.as_view(), name='password_change'),
]


