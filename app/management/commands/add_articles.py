import json
import requests
import os
from newsapi import NewsApiClient
from app.models import Article
from django.core.management.base import BaseCommand



class Command(BaseCommand):

    #API for all other news sources

    def handle(self,*args,**options):
        Article.objects.all().delete()
        client = NewsApiClient(api_key = os.environ.get("NEWS_API_KEY"))
        top_headlines = client.get_top_headlines(language='en',page_size=100)
        articles = top_headlines['articles']
        for article in articles:
            a = Article(title=article['title'],url=article['url'],source = article['source']['name'],date_posted = article['publishedAt'][:10],url_to_image =article["urlToImage"])
            a.save()

        
        # Special API for The New York Times

        r = requests.get("https://api.nytimes.com/svc/topstories/v2/home.json?api-key={}".format(os.environ.get("NYT_API_KEY")))
        r = json.loads(r.text)
        for article in r['results']:
            title = article['title']
            url = article['url']
            url_to_image = article['multimedia'][3]['url']
            date_posted = article['updated_date'][:10]
            a = Article(title=title,url=url,source="The New York Times",date_posted=date_posted,url_to_image=url_to_image)
            a.save()

        # Special API for The Guardian

        r = requests.get("https://content.guardianapis.com/search?q=football&api-key={}&order-by=newest&show-fields=thumbnail,trailText".format(os.environ.get("GUARDIAN_API_KEY")))
        r = json.loads(r.text)['response']['results']
        for article in r:
            title = article['webTitle']
            url = article['webUrl']
            url_to_image = article['fields']['thumbnail']
            date_posted = article["webPublicationDate"][:10]
            a = Article(title=title,url=url,source="The Guardian",url_to_image=url_to_image,date_posted=date_posted)
            a.save()
        