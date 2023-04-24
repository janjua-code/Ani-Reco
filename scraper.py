import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url)
response = response.content

soup = BeautifulSoup(response, 'html.parser')
ol = soup.find('ol')
article = ol.find_all('article', class_='product pod')
print(soup)