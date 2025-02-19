from django import forms

class Feedback_Form(forms.Form):
    Name=forms.CharField()
    Rollno=forms.IntegerField()
    Email=forms.EmailField()
    Feedback=forms.CharField(widget=forms.Textarea)