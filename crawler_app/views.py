from crawler_app.crawler import Crawler
from django.shortcuts import render
from django.http import HttpResponse


def index(requests):
    web_crawler = Crawler()
    web_crawler.get_html()
    return HttpResponse({'status': True})




