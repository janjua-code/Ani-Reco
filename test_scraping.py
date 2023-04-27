import requests
from bs4 import BeautifulSoup


def sample_scraper() -> None:
    """First scraper"""
    url = "https://books.toscrape.com/catalogue/page-1.html"
    response = requests.get(url)
    response = response.content

    soup = BeautifulSoup(response, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')

    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']

        star = article.find('p')
        print(star)
        star = star['class'][1]

        price = article.find('p', class_='price_color').text

