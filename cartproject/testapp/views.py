from django.shortcuts import render
from .import forms
# Create your views here.
def add_item_view(request):
    form=forms.additemsform()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
        request.session.set_expiry(120)
    return render(request,'additems.html',{'form':form})

def display_item_view(request):
    return render(request,'displayitems.html')


def session_info_view(request):
    session=request.session
    age=session.get_expiry_age()
    date=session.get_expiry_date()
    print('expiry age ',age)
    print('expiry date',date)
    return render(request,'additems.html')
    