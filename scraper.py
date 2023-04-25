import requests
from bs4 import BeautifulSoup
from entry import AnimeEntry


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


def mal_scraper(pages: int, link: str) -> None:
    """MyAnimeList anime data Scraper"""
    l = len(link)
    for i in range(1, 2):
        link = link[:l - 2] + str(i)
        response = requests.get(link)
        response = response.content

        soup = BeautifulSoup(response, 'html.parser')
        anime_lst = soup.find("div", {"seasonal-anime-list"})
        articles = anime_lst.find_all('div', class_='title')

        for article in articles:
            title = article.find('a')
            name = title.text
            lnk = title['href']

            score = article.find('span', class_='js-score').text
            score = float(score)
            if score == 0:
                score = None

            recos = get_recommendations(lnk)
            tags = get_tags(lnk)
            anime = AnimeEntry(name, lnk, [], score, [])
            print(anime)


def get_recommendations(link: str) -> list[str]:
    """Return a list of all recommendations given the <link> to an anime"""
    pass


def get_tags(link: str) -> list[str]:
    """Return a list of all genres, themes, and demographic given the <link> to
    an anime"""
    pass


if __name__ == "__main__":
    mal_scraper(3, "https://myanimelist.net/anime/genre/41/Suspense?page=1")
    # sample_scraper()

