from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
 
 #django form we are using because we dont want to create another html template rather than this we are using django's power for templates and forms.
 #to make the forms first we have to import forms and models then create a class and remember there will always be a Meta class and fields in which we have to select the fields.
 
class Tweetform(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','photo']
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')                     #here we are using inbuilt form in djnago so that we will select fields by using tuple and if we made a model so we select fields by array.
        
#after making form goto views.py