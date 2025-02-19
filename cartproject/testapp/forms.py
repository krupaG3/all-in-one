from django import forms 

class additemsform(forms.Form):
    name=forms.CharField()
    quantity=forms.IntegerField()