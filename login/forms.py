from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import fields



class CreateUserFrom(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = '__all__'