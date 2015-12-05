from django import forms

class UserForm(forms.Form): 
	name = forms.CharField(label='user_name', max_length=100)
	password = forms.CharField(label='password', max_length=100)