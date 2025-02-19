from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def moviesinfo(request):
    head_msg='Latest movie iformation'
    msg1='sonali slowly getting cured'
    msg2='salman going to marraige soon'
    msg3='modi is going to act in some movie'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'news.html',context=my_dict)


def sportsinfo(request):
    head_msg='Latest sports iformation'
    msg1='krupa was all Rounder'
    msg2='mani was bowler'
    msg3='ravi was batsman'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'news.html',context=my_dict)



def politicsinfo(request):
    head_msg='Latest politics iformation'
    msg1='e saari ap ki maadde'
    msg2='telanagan was very unlucky'
    msg3='me always unlucky'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'news.html',context=my_dict)
