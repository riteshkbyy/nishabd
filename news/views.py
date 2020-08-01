from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, HttpResponse
from rest_framework import generics, status
from .models import Feed, Article
from .forms import FeedForm
from .tasks import update_all_feed_articles_task
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


@login_required(login_url = "user:login")
def update_articles(request):
    update_all_feed_articles_task()
    return redirect('news:articles-list')
        