from data_get import get_content
from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import requests


class Command(BaseCommand):

    def handle(self, *args, **options):
        print page_scrape(args)

def page_scrape(args):

    url="http://www.imdb.com/search/title?at=0&count=100&sort=num_votes"
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    for link in soup.find_all('a'):
        url = str(link.get('href'))
        title = link.get('title')
        if url[0:7] == '/title/':
            try:
                title = str(title)
                if 'TV Series' in title or 'Mini-Series' in title or 'Short Film' in title or 'Documentary' in title or 'TV Movie' in title or 'Video' in title:
                    pass
                elif '(' in title:
                    print url[len(url)-10:len(url)-1]
                    page_url = 'http://www.imdb.com' + url
                    page_r = requests.get(page_url)
                    page_soup = BeautifulSoup(page_r.content)
                    # print page_soup.find('span',itemprop="ratingValue").string
                    # print page_soup.find(itemprop="datePublished")['content']
                    # print page_soup.find('time', itemprop="duration").string.strip()
                    

                    # for director in page_soup.find_all('div', itemprop="director"):
                    #     print director.find('a')['href'][:15]
                    #     print director.find('a').string
                    # for writer in page_soup.find_all('div', itemprop="creator"):
                    #     print writer.find('a')['href'][:15]
                    #     print writer.find('a').string
                    # for actor_even in page_soup.find_all('tr', 'even'):
                    #     if actor_even.find('td', itemprop="actor") != None:
                    #         print actor_even.find('td', itemprop="actor").find('a')['href'][:16]
                    #         print actor_even.find('td', itemprop="actor").find('span').string
                    #         try:
                    #             print actor_even.find('td', class_="character").find('a')['href'][:21]
                    #             print actor_even.find('td', class_="character").find('a').string
                    #         except TypeError:
                    #             pass
                    #     else:
                    #         pass
                    # for actor_odd in page_soup.find_all('tr', 'odd'):
                    #     if actor_odd.find('td', itemprop="actor") != None:
                    #         print actor_odd.find('td', itemprop="actor").find('a')['href'][:16]
                    #         print actor_odd.find('td', itemprop="actor").find('span').string
                    #         try:
                    #             print actor_odd.find('td', class_="character").find('a')['href'][:21]
                    #             print actor_odd.find('td', class_="character").find('a').string
                    #         except TypeError:
                    #             pass
                    #     else:
                    #         pass
                    break
            except UnicodeEncodeError:
                pass
