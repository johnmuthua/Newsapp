from django.shortcuts import render
from .models import NewsArticle
from .config import API_KEY
import requests
import json

# Create your views here.
def about(request):
    context = NewsArticle.objects
    return render(request, 'about.html', {"context":context})

def home(request):
    context = NewsArticle.objects
    return render(request,'home.html', {"context":context})

def update(request, KEY = API_KEY, country='us'):
    #TODO check if there is internet connection
    #TODO place the code within a try catch block
    #TODO try to detect  duplicates
    KEY = API_KEY
    url = ('https://newsapi.org/v2/top-headlines?'
           'country='+ country+ '&'
           'apiKey=' + KEY)
    print(KEY)
    print(url)
    response = requests.get(url)
    data = response.json()['articles']
    for news in data:
        n = NewsArticle(source = news['source'],author = news['author'],
                        title= news['title'], description = news['description'], url= news['url'],
                        urlToImage = news['urlToImage'], publishedAt = news['publishedAt'],
                        content = news['content'],)
        if n:
            n.save()
    return render(request,'update.html', {"data":data[0]})
