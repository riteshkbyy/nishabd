from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import RegisterForm,LoginForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import *




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
        return redirect("article:profile")
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
        try:
            return redirect(request.GET['next'])
        except:
            pass
        return redirect("article:dashboard")
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request,"Logout Success")
    return redirect("article:articles")


@login_required(login_url = "user:login")
def Profile(request):    
    user = get_object_or_404(UserProfile, user=request.user)
    # user = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    form= ProfileForm(request.POST or None, request.FILES or None,instance = user)
    if form.is_valid():
        profile = form.save(commit=False)
        # pro.slug = slugify(article.title)
        profile.user = request.user
        profile.save()
        return redirect("user:profile")
    return render(request,"profile.html",{"form":form})
