from django import forms
from .models import *

class user_std_form(forms.Form):
    name = forms.CharField() 
    age = forms.IntegerField()
    mark = forms.IntegerField() 
    
class model_form(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'