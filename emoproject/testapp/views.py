from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')


def Movies_View(request):
    msg1='hello movies'
    msg2='hello movies'
    msg3='hello movies'
    my_dict={'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'testapp/view.html',context=my_dict)

def Sports_View(request):
    msg1='hello sports'
    msg2='hello sports'
    msg3='hello sports'
    my_dict={'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'testapp/view.html',context=my_dict)

def Jobs_View(request):
    msg1='hello jobs'
    msg2='hello jobs'
    msg3='hello jobs'
    my_dict={'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'testapp/view.html',context=my_dict)
