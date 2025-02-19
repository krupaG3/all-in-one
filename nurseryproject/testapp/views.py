from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    name='krupa' 
    h=int(date.strftime('%H'))
    if h<12:
        msg=' good morning'
    elif h<16:
        msg=' good afternoon'
    elif h<21:
        msg=' good evening'
    else:
        msg=' good night'
    
    my_dict={'name':name,'date':date,'msg':msg}
    return render(request,'wish.html',context=my_dict)