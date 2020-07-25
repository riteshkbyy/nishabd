from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout



# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        e_mail = form.cleaned_data.get('email')

        newUser = User(username =username, email = e_mail)
        newUser.set_password(password)
        

        newUser.save()
        login(request,newUser)
        messages.info(request,str(username) + " Registered successfully")

        return redirect("article:dashboard")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)

    
    
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Invalid Credentials")
            return render(request,"login.html",context)

        messages.success(request,"Login Success")
        login(request,user)
        return redirect("article:dashboard")
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request,"Logout Success")
    return redirect("article:articles")

