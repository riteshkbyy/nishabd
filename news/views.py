from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, HttpResponse
from rest_framework import generics, status
from .models import Feed, Article
from .forms import FeedForm
from background_task import background
from django.contrib.auth.models import User

# Create your views here.
def articles_list(request, feed_id=None):

    if feed_id is None:
        feed = Feed.objects.all()
    else:
        feed = None
    
    form = FeedForm
        
    context = {
        'feed': feed,
        'form': form,
    }
    
    return render(request, "articles_list.html", context)

def feeds_list(request):
    feeds = Feed.objects.all()
    form = FeedForm
    
    context = {
        'feeds': feeds,
        'form': form,
    }
    
    return render(request, "feeds_list.html", context)
    
@login_required(login_url = "user:login")
def new_feed(request):
    if request.method == "POST":
        # Process our form
        form = FeedForm(request.POST)
        
        if form.is_valid():
            feed = form.save(commit=False)
            feed.save()
                
            return redirect('news:feeds-list')
    else:
        form = FeedForm
    
    context = {
        'form': form,
    }
    
    return render(request, "new_feed.html", context)



        