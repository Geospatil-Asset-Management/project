from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Task.models import Task



class LoginForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Password",widget = forms.PasswordInput)
    username = forms.CharField(label = "Kullanici Adi")
    password = forms.CharField(label = "Parola",widget = forms.PasswordInput)

    

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=32)
    first_name = forms.CharField(max_length=32)
    last_name=forms.CharField(max_length=32)
    email=forms.EmailField()
    password1=forms.CharField(label = "Password",widget = forms.PasswordInput)
    password2=forms.CharField(label = "Confirm Password",widget = forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email','password1','password2']


class TaskForm(forms.ModelForm):
    class Meta :
        model = Task
        fields = ["task_type","name","assigned_by","assigned_to","description"]



