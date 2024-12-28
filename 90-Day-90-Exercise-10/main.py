import requests
from bs4 import BeautifulSoup
import json

# sortby=keywords
# url = ('https://newsapi.org/v2/everything?'
#        'q=Apple&'
#        'from=2024-12-28&'
#        'sortBy=popularity&'
#        'apiKey=48f1f32b7d254f39ab6929b2d7a46a35')

#country Wise
# url = ('https://newsapi.org/v2/top-headlines?'
#        'country=us&'
#        'apiKey=48f1f32b7d254f39ab6929b2d7a46a35')

# url = ('https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=48f1f32b7d254f39ab6929b2d7a46a35')

# #BBC News
# url = ('https://newsapi.org/v2/top-headlines?'
#        'sources=bbc-news&'
#        'apiKey=48f1f32b7d254f39ab6929b2d7a46a35')

query = input("What type of news you are interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-11-28&sortBy=publishedAt&apiKey=48f1f32b7d254f39ab6929b2d7a46a35"
response = requests.get(url)
news = response.json()
for articles in news["articles"]:
    print(f"source: {articles['source']['name']}")
    print(f"Title: {articles['title']}")
    print(f"descdescription: {articles['description']}")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")

# print(news,type(news))

# print(response.json())
# soup = BeautifulSoup(response.text,'html.parser')
# print(soup.prettify())
# print(response.text)