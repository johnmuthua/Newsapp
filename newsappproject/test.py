import requests
country = 'us'
KEY = 'fa22f16f499743189d15691ded47f60b'
url = ('https://newsapi.org/v2/top-headlines?'
           'country='+ country+ '&'
           'apiKey=' + KEY)
response = requests.get(url).json()
print(response)