from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead
from .Allchoise import *

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'agent',
            'source',
            'message',
        )

class LeadForm(forms.Form):
    first_name = forms.CharField().attrs={'class': 'form-control'}
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    source = forms.ChoiceField(choices=(SOURCE_CHOICES))
    message = forms.CharField(widget=forms.Textarea)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        field_classes = {'username': UsernameField}

        
