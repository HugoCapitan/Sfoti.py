from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserCreationEmailForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ('username', 'email')


	def clean_email(self):
		email = self.cleaned_data.get('email')
	 	try:
	 		User.objects.get(email = email)
	 		raise forms.ValidationError('Email Repetido')
	 	except User.DoesNotExist:
	 		return email

	def get_authentication_data(self):
		authentication_data = {'username': self.cleaned_data.get('username'), 'email': self.cleaned_data.get('email'), 'password': self.cleaned_data.get('password1')}
		return authentication_data


class EmailAuthenticationForm(forms.Form):
	email = forms.EmailField();
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		self.user_cache = None
		super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

	def clean(self):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')

		self.user_cache = authenticate(email=email, password=password)

		if self.user_cache is None:
			raise forms.ValidationError('Usuario incorrecto')
		elif not self.user_cache.is_active:
			raise forms.ValidationError('Usuario inactivo')

		return self.cleaned_data


	def get_user(self):
		return self.user_cache