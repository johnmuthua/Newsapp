from django.shortcuts import render
from .models import NewsArticle
from .config import API_KEY
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def about(request):
    context = NewsArticle.objects.all()
    return render(request, 'about.html', {"context":context[0]})

def home(request):
    all_news = NewsArticle.objects.all()
    paginator = Paginator(all_news, 9)
    page = request.GET.get('page',1)
    
    try:
        news = paginator.get_page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request,'home.html', {"context":news})

def update(request, KEY = API_KEY, country='us'):
    payload = {}
    #Get the latest news
    try:
        KEY = API_KEY
        url = ('https://newsapi.org/v2/top-headlines?'
               'country=' + country + '&'
                                      'apiKey=' + KEY)
        print(KEY)
        print(url)
        response = requests.get(url)
        data = response.json()['articles']
    except Exception as e:
        payload['message'] = "http request failed!"
        payload['error'] = e
        return payload

    for news in data:
        #Populate the database with the latest news
        n, created = NewsArticle.objects.get_or_create(source = news['source'],author = news['author'],
                        title= news['title'], description = news['description'], url= news['url'],
                        urlToImage = news['urlToImage'], publishedAt = news['publishedAt'],
                        content = news['content'],)
        print(news['publishedAt'])
        if n:
            payload['update']="Database updated successfully"
            n.save()
        else:
            payload['update'] = "Database update Failure"
    return render(request,'update.html', {"payload":payload})

