from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserModel

# Create your views here.
from .models import *
from .forms import  CreateUserForm, UserForm

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'user/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'user/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')



def userPage(request):

	
	return render(request, 'user/user.html')

def accountSettings(request):
	user = request.user
	form = UserForm(instance=user)

	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES,instance=user)
		if form.is_valid():
			form.save()

	context = {'form':form}
	return render(request, 'user/user.html', context)

