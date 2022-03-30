from django import forms
from django.contrib.auth.models import User
from django.forms import fields, widgets
from blog import models
from blog.models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


class User_Signup(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }

class User_Login(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.Textarea(attrs={'class':'form-control'}),
        }