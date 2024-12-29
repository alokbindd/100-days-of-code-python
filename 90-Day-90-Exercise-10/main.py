import requests,creds,json
from datetime import datetime,timedelta
from bs4 import BeautifulSoup

# sortby=keywords
# url = ('https://newsapi.org/v2/everything?'
#        'q=Apple&'
#        'from=2024-12-28&'
#        'sortBy=popularity&'
#        f'apiKey={creds.api_key}')
       

#country Wise
# url = ('https://newsapi.org/v2/top-headlines?'
#        'country=us&'
#        f'apiKey={creds.api_key}')

# url = (f'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey={creds.api_key}')

# #BBC News
# url = ('https://newsapi.org/v2/top-headlines?'
#        'sources=bbc-news&'
#        f'apiKey={creds.api_key}')

date = (datetime.today() - timedelta(days=30)).strftime("%Y-%m-%d")
query = input("What type of news you are interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from={date}&sortBy=publishedAt&apiKey={creds.api_key}"
response = requests.get(url)
news = response.json()
# print(news,type(news))
for articles in news["articles"]:
    print(f"source: {articles['source']['name']}")
    print(f"Title: {articles['title']}")
    print(f"descdescription: {articles['description']}")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")


# print(response.json())
# soup = BeautifulSoup(response.text,'html.parser')
# print(soup.prettify())
# print(response.text)