from django import forms
from .models import User

class CreateUserForm(forms.Form):
	class Meta:
		model = User
		fields = ['first_name', 'last_name',]