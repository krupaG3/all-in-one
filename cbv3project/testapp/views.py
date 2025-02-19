from django.shortcuts import render
from django.views.generic import View,ListView,DetailView
from testapp.models import Company_Model
# Create your views here.

class Company_View(ListView):
    book=Company_Model