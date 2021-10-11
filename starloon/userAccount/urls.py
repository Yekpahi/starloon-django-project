from django.urls import path
from . import views
from userAccount.views import ChangePasswordView


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('profile/', views.profile, name='users-profile'),
	path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]


