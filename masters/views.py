import requests
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
from . import models

BASE_HOBBY_URL = 'https://losangelas.craiglist.org/search/?query={}'


# Create your views here.

def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    #print(quote_plus(search))
    final_url = BASE_HOBBY_URL.format(quote_plus(search))

    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data,features='html.parser')
    post_titles = soup.find_all('a',{'class':'result-title'})
    print(post_titles[0].text)
    #print(data)
    print(search)
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'masters/new_search.html', stuff_for_frontend)
