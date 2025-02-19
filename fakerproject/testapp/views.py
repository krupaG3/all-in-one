from django.shortcuts import render
from testapp.models import *
from .import forms

# Create your views here.
def Home_View(request):
    a=forms.Feedback_Form()
    return render(request,'testapp/feedback.html',{'a':a})

def Output_View(request):
    form=forms.Feedback_Form()
    if request.method=='POST':
        form=forms.Feedback_Form(request.POST)
        if form.is_valid():
            print('sucesss')
            print('student name',form.cleaned_data['Name'])
            print('student Feedback',form.cleaned_data['Feedback'])
    return render(request,'testapp/index.html',{'form':form})

