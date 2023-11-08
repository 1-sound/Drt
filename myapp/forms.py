from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    verification_code = forms.CharField(label="인증 코드", required=True)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "verification_code")