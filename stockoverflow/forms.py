from django import forms
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,

)
from .models import Contact
User = get_user_model()



class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			}

		))
	password = forms.CharField(widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
			}

		))

	def clean(self, *args, **kwargs):
			username = self.cleaned_data.get("username")
			password = self.cleaned_data.get("password")
			#user_qs = User.objects.filter(username=username)
			#if user_qs.count() == 1:
			#		user = user_qs.first()
			if username and password:
				user = authenticate(username=username,password=password)	
			if not user:
				raise forms.ValidationError("This user does not exist")

			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password")

			if not user.is_active:
				raise forms.ValidationError("User in not active")
			return super(UserLoginForm,self).clean(*args,**kwargs)

class UserRegisterForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			}

		))
	email = forms.EmailField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			}

		))
	confirmpassword = forms.CharField(widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
			}

		))
	password = forms.CharField(widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
			}


		))
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password',
			'confirmpassword',
		]			
	def clean(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		confirmpassword = self.cleaned_data.get('confirmpassword')
		if password != confirmpassword:
			raise forms.ValidationError("Password Should be same")
		email_qs = User.objects.filter(email="email")
		if email_qs.exists():
			raise forms.ValidationError("This email has already been registered")
		return super(UserRegisterForm,self).clean(*args,**kwargs)


class Contactform(forms.ModelForm):
	name= forms.CharField()
	email= forms.CharField()
	phno= forms.IntegerField()
	message= forms.CharField()

	class Meta:
		model = Contact
		fields=[
			'name',
			'email',
			'phno',
			'message',

		]
	def clean(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		name = self.cleaned_data.get('name')
		phno = self.cleaned_data.get('phno')
		message = self.cleaned_data.get('message')