from django.shortcuts import render

# Create your views here.
def hellodjango(request):
    dl ={
        'name':'harshitha',
        'email':"harshitha@gmail.com",
        'l1':[1,2,3,4],
        'd2':{'city':'bangalore','adress':'btm'}


    }

    return render(request,'hello.html',dl)


def welcomedjango(request):
    return render(request,'welcome.html')