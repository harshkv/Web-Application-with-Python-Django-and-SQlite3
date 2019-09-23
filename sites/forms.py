from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import ValidationError
from django.contrib.auth.models import User


def checkEmail(value):
    try:
        User.objects.get(email=value)
        raise ValidationError("Email already exists")
    except User.DoesNotExist:
        pass
    except User.MultipleObjectReturned:
        raise ValidationError("email already exists")


def validateEmail(email):
    try:
        User.objects.get(email=email)
    except User.DoesNotExist:
        raise ValidationError("invalid user!")


class LoginForm(forms.Form):
    username = forms.CharField(max_length= 20 )
    password = forms.CharField(
        max_length =20,
        widget = forms.PasswordInput()
    )


class RegisterForm(UserCreationForm):
    email = forms.EmailField(validators=[checkEmail])
    password1 = forms.CharField(min_length =8,
                                max_length= 20,
                                widget =forms.PasswordInput)



class SignUpForm(forms.Form):
    username =forms.CharField(max_length = 20)
    email = forms.EmailField()
    password1 = forms.CharField(label = 'password',
                                min_length=8,
                                max_length=20,
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'password-confirm',
                                min_length=8,
                                max_length=20,
                                widget=forms.PasswordInput)
    def clean(self):
        form_data =self.cleaned_data
        if 'password1' in form_data and 'password2' in form_data:
            if( form_data['password1'] != form_data['password2']):
                self.errors['password2'] =["Password Missmatch!"]
        return form_data



class ForgotPassword(forms.Form):
    email = forms.EmailField(validators =[validateEmail])
    password1 = forms.CharField(min_length=8,
                                max_length=20,
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='password-confirm',
                                min_length=8,
                                max_length=20,
                                widget=forms.PasswordInput)
    def clean(self):
        form_data =self.cleaned_data
        if 'password1' in form_data and 'password2' in form_data:
            if( form_data['password1'] != form_data['password2']):
                self.errors['password2'] =["Password Missmatch!"]
        return form_data
