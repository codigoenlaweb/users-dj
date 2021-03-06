from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("first_name", "last_name", "username", "email", "password1", "password2")

	def save(self):
		user = super(RegisterUserForm, self).save()
		return user

