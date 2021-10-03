from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserModel
from django import forms


class UserForm(ModelForm):
	class Meta:
		model = UserModel
		fields = '__all__'
		exclude = ['user']
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']