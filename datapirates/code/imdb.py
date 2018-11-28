# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re
import json
def extract_genres(self, response):	
    ''' Extract genre list from imdb, getting genre list from 
        https://www.imdb.com/search/title,so if genre list change
        because of some reason this scripting don't need to be
        a changed.
	
       :param self: Instance of the class ImdbSpider
       :param response: The Response object from scrapy
       :return: returns genres list
    '''
    genres = []
    index = 1
    for genre in response.css('div.clause:nth-of-type(6) table'):
        soup = BeautifulSoup(genre.extract())
        index += 1
        genres = [str(genre).replace(' ', '') for genre in soup.get_text().split('\n') if str(genre) != '']
    return genres

def generate_urls(genres):
    '''Generate a list of URLs to search sorted by 'Rating'.
	
       :param genres: genre list of IMDB 
       :return: returns URLs list to search
    '''
    genre_list_to_search = []
    for genre in genres:
        start = 1
        for next in range(0, 10):
            url = 'https://www.imdb.com/search/title?genres={}&sort=user_rating,desc&start={}&ref_=adv_nxt'.format(genre, start)
            genre_list_to_search.append(url)
            start += 50
    return genre_list_to_search

def extract_genre_from_url(url):
    '''Extract genre from url.
	
       :param url: url which will be extracted genre
       :return: returns genre
    '''
    s = 'asdf=5;iwantthis123jasd'
    return re.search('genres=(.*)&sor', url).group(1)

def add_jsonl(title):
    '''Add the title to the jsonl specific file per genre.
	
       :param title: which will be add to the jsonl specific file
       :return: returns anything "void"
    '''
    with open('{}.jsonl'.format(title['genre']), 'a') as outfile:
        json.dump(title, outfile)
        outfile.write('\n')
        outfile.close()

class ImdbSpider(scrapy.Spider):
    '''ImdbSpider is a Spider class from Scrapy with informations
       how to scrape information from IMDB 
    '''  
    name = 'imdb_spider'
    start_urls = ['https://www.imdb.com/search/title']

    def parse(self, response):
        urls = generate_urls(extract_genres(self, response))

        for url in urls:
            yield scrapy.Request(url, self.handle_extract)

    def handle_extract(self, response):
        self.log('URL: {}'.format(response.url))
        for item in response.css('div.lister-item'):
            item_extract = {
                'image': item.css('img.loadlate::attr("loadlate")').extract_first(),
                'title': ''.join(e for e in item.css('h3.lister-item-header a::text').extract()),
                'rating': float(item.css('div.inline-block.ratings-imdb-rating::attr("data-value")').extract()[0]),
                'votes': int(item.css('p.sort-num_votes-visible span::attr("data-value")').extract()[0]),
                'genre': extract_genre_from_url(response.url)
            }
            add_jsonl(item_extract)
            
