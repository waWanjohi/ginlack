from django.forms import ModelForm, EmailField, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    first_name = TextInput()
    last_name = TextInput()
    email = EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class UserUpdateForm(ModelForm):
    email = EmailField()
    class Meta:
        model = User
        fields = ['email', 'username']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

