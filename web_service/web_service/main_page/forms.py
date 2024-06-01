from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
        username = forms.CharField(max_length=45, required=True, label='Логин', widget = forms.TextInput(attrs={'class': 'form-input'}))
        password1 = forms.CharField(max_length=45, required=True, label='Пароль', widget = forms.PasswordInput(attrs={'class': 'form-input'}))
        password2 = forms.CharField(max_length=45, required=True, label='Подтверждение пароля', widget = forms.PasswordInput(attrs={'class': 'form-input'}))
        first_name = forms.CharField(max_length=45, required=True, label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
        last_name = forms.CharField(max_length = 45, required=True, label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
        email = forms.CharField(max_length=45, required=True, label='Электронная почта', widget=forms.TextInput(attrs={'class': 'form-input'}))
        phone = forms.CharField(max_length=11, required=True, label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-input'}))
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone')
        widgets = {
                'username': forms.TextInput(attrs={'class': 'form-input'}),
                'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
                'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
                'first_name': forms.TextInput(attrs={'class': 'form-input'}),
                'last_name': forms.TextInput(attrs={'class': 'form-input'}),
                'email': forms.TextInput(attrs={'class': 'form-input'}),
                'phone': forms.TextInput(attrs={'class': 'form-input'})
        }

class LoginUserForm(forms.Form):
        username = forms.CharField(max_length=45, required=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
        password = forms.CharField(max_length=45, required=True, label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class AddController(forms.Form):
        name = forms.CharField(max_length=45, required=True, label='Назовите контроллер', widget = forms.TextInput(attrs={'class': 'form-input'}))
        fields = ('Name')
