from django import forms
from .models import User,Taskmodel

class User_reg(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Last Name'}),
            'email':forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Email'}),
            'password':forms.PasswordInput(attrs={'class':'form-control form-control-lg','placeholder':'Password'})
        }
    
class Task_reg(forms.ModelForm):
    class Meta:
        model=Taskmodel
        fields=['task_name','task_description']
        widgets={
            'task_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Task Name'}),
            'task_description':forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Description'}),
        }
    
class Login_form(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg my-3','placeholder':'Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg my-3','placeholder':'Password'}))

class User_edit(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Last Name'}),
            'email':forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Email'}),
        }
    