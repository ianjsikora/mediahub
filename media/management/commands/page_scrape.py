from data_get import get_content
from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import requests


class Command(BaseCommand):

    def handle(self, *args, **options):
        print page_scrape(args)

def page_scrape(args):

    url="http://www.imdb.com/search/title?at=0&count=1&sort=year,desc&start=17461&title_type=feature,tv_series,tv_movie"
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    links = soup.find_all('a')
    id_list = []
    for link in links:
        if link.get('href').find('title/tt') > 0 and len(link.get('href')) == 17:
            if link.get('href')[7:16] in id_list:
                print 'skip'
            else:
                id_list.append(link.get('href')[7:16])
    print id_list
    print get_content(id_list)