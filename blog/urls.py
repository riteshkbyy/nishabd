"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from article import views
from rest_framework.urlpatterns import format_suffix_patterns
from news import views as news_views
from news.api import ArticlesList
from news.views import articles_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name = "index"),
    path('about/',views.about,name = "about"),
    path('article/',include("article.urls")),
    path('user/',include("user.urls")),
    url(r'^$', articles_list, name='articles-list'),
    url(r'^news/', include('news.urls')),
    # REST API URLs
    url(r'^api/$', ArticlesList.as_view()),
    url(r'^api/news/articles/$', ArticlesList.as_view()),
    url(r'^api/news/feeds/(?P<feed_id>[0-9]+)/$', ArticlesList.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)