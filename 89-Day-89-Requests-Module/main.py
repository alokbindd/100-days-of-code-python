import requests
from bs4 import BeautifulSoup
# url= "https://www.google.com"
# url = "https://www.github.com/alokbind01"
url = "https://jsonplaceholder.typicode.com/posts"

header = {"user":"myagent","content":"coder"}
data= {
    "Name":"Alok",
    "Userid": 1,
    "subject": "Python"
}

response = requests.post(url,headers=header,json=data)
print(response.text)


response = requests.get(url)
print(response.status_code)
print(response.text)
soup = BeautifulSoup(response.text,'html.parser')
print(soup.prettify())

