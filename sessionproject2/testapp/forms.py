from  django import forms 

class nameform(forms.Form):
    name=forms.CharField()

class ageform(forms.Form):
    age=forms.IntegerField()
    
class gfform(forms.Form):
    gf=forms.CharField()