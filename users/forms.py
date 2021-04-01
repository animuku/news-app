from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from newsapi import NewsApiClient

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    client = NewsApiClient(api_key = "36f720b2539b4900bcfef79c06fe699b")
    sources = client.get_sources()['sources']
    list = []
    for source in sources:
        list.append((source['name'],source['name']))
    list.append(("The New York Times","The New York Times"))
    list.append(("The Guardian","The Guardian"))
    OPTIONS = tuple(list)
    sources = forms.MultipleChoiceField(widget=forms.SelectMultiple,choices=OPTIONS)
    
    def clean_sources(self):
        field = ""
        for data in self.cleaned_data['sources']:
            field += str(data)+","
        return field.rstrip(",")
    
    class Meta:
        model = Profile
        fields = ['image','sources']

    
        