from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth import authenticate

from .forms import UserCreationEmailForm, EmailAuthenticationForm


def signup(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()
		authentication_data = form.get_authentication_data()
		# email = form.get_email()
		# password = form.get_password()
		user = authenticate(email = authentication_data['email'], password = authentication_data['password'])
		login(request, user)

	return render(request, 'signup.html', {'form': form})

def signin(request):
	form = EmailAuthenticationForm(request.POST or None)

	if form.is_valid():
		login(request, form.get_user())

	return render(request, 'signin.html', {'form': form})
