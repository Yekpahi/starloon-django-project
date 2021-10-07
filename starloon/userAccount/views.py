from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
from .models import *
from .forms import  CreateUserForm

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				username  = form.cleaned_data.get('username')

				messages.success(request, 'Account was created for ' + profile)

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


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'user/profile.html', {'user_form': user_form, 'profile_form': profile_form})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'user/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('index')

