from django.shortcuts import render, redirect

from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sites.forms import LoginForm,RegisterForm,SignUpForm,ForgotPassword



def userRegistration(request):
    # form= UserCreationForm()
    form = RegisterForm()
    message = ""
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.username = username
            user.email = form.cleaned_data['email']
            user.set_password(password)    #password hash key
            #user.password = password  #raw password
            user.save()
            message = 'registration done successfully!'


    return render(request,'sites/registration.html',{'form':form, 'msg': message})

def forgotPassword(request):
    message =""
    form = ForgotPassword()
    if request.method == 'POST':
        form =ForgotPassword(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password1']
            email =form.cleaned_data['email']
            user = User.objects.get(email = form.cleaned_data['email'])
            user.set_password(password)
            user.save()
            message ='password reset done successfully'

    return render(request,'sites/forgot_password.html',{'form':form,'msg': message})


def userLogin(request):
    if request.user.username:
        redirect(userDashboard)
    form = LoginForm()
    message =''
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
            username = username,
            password = password
            )
            print(user)
            if user is None:
                message = ' User is not found!'
            else:
                login(request,user)
                request.session['city'] = 'Bangalore'
                return redirect(userDashboard)

    return render(request, 'sites/login.html', {'form': form, 'msg': message})


def userDashboard(request):
    return render(request, 'sites/dashboard.html')




def userLogout(request):
    logout(request)
    return redirect(userLogin)


def staticExamples(request):
    return render(request,'sites/static_example.html')