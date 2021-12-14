from django.contrib.auth import login,logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm


def signup_view (request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
           user= form.save() 
           login(request,user)
    form = UserCreationForm()
    return render (request, 'accounts/signup.html',{'form':form})

def login_view (request):
    if request.method == "POST":
        form=AuthenticationForm(data =request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
        return redirect('/')
    form =AuthenticationForm()
    return render (request,'accounts/login.html',{'form':form})

def logout_view (request):
    if request.method == "POST":
        logout(request)
    return redirect('/')
