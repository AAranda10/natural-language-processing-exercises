import pandas as pd
from requests import get
from bs4 import BeautifulSoup
import os

################################ Acquire Blogs #################################

def get_blogs(websites, cached = False):
    
    if cached == True:
        
        blogs = pd.read_json('blogs.json')
        
    else:
        
        blogs = []        
        for blog in websites:
            headers = {'User-Agent': 'Codeup Data Science'}
            response = get(blog, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            page = soup.find('div', class_='jupiterx-post-content')
            article = {'title':[], 'body':[]}
            article['title'] = soup.title.string
            article['body'] = page.text
            blogs.append(article)    
        blogs = pd.DataFrame(blogs)
        blogs.to_json('blogs.json')
        
    return blogs

################################ Acquire Codeup Blog Articles #################################

def get_inshorts(websites, cached=False):

    if cached == True:
        articles = pd.read_json('articles.json')

    else:
        
        articles = []
        
        for article in websites:
            
            article_dict = {'headline':'','author':'','date':'','article':'','category':''}
            
            headers = {'User-Agent': 'Inshorts'}
            data = get(article, headers)
            soup = BeautifulSoup(data.text, "html.parser")
            article_structure['title'] = soup.find('span', attrs={"itemprop": "headline"}).string
            article_structure['author'] = soup.find('span', attrs={"author"}).string
            article_structure['body'] = soup.find('div', attrs={"itemprop": "articleBody"}).string
            article_structure['date'] = soup.find('span', attrs={"date"}).string
            article_structure['category'] = url.split('/')[-2]
            articles.append(article_structure)
            
        articles = pd.DataFrame(articles)
        articles = articles[['title', 'author','body','date', 'category']]
        articles.to_json('articles.json')
        
    return articles