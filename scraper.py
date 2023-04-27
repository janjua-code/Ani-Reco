from typing import Any

import requests
from bs4 import BeautifulSoup
from entry import AnimeEntry


def mal_scraper(pages: int, link: str) -> None:
    """MyAnimeList anime data Scraper.
    ===DevLog===
    Now scrapes data from certain genres from "https://myanimelist.net/anime.php"
    given number of pages
    """
    l = len(link)
    for i in range(1, pages + 1):
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

            anime_response = requests.get(lnk).content
            # to reduce the amount of requests we are making for the next two
            # functions
            pop = get_popularity(anime_response)
            tags = get_tags(anime_response)
            recs = get_recommendations(lnk)

            anime = AnimeEntry(name, lnk, score, pop, tags, recs)
            print(anime)


def get_recommendations(link: str) -> list[str]:
    """Get recommendations of anime given <link>"""
    response = requests.get(link + '/userrecs')
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')
    reco_list = soup.find_all('div', class_='borderClass')
    lst = []
    for reco in reco_list:
        title = reco.find('strong')
        if title is not None:
            title = title.text
            lst.append(str(title))
    return lst


def get_tags(response: Any) -> list[str]:
    """Return a list of all genres, themes, and demographic given the <link> to
    an anime"""
    soup = BeautifulSoup(response, 'html.parser')
    lst = []
    g = soup.find_all('span', itemprop='genre')
    for genre in g:
        lst.append(str(genre.text))
    return lst


def get_popularity(response: Any) -> int:
    """Return popularity of anime"""
    soup = BeautifulSoup(response, 'html.parser')
    pop = soup.find('span', class_='numbers popularity').find('strong').text[1:]
    return int(pop)


if __name__ == "__main__":
    # l = 'https://myanimelist.net/anime/16498/Shingeki_no_Kyojin'
    # response = requests.get(l).content
    # r = get_tags(response)
    # print(r)
    mal_scraper(3, "https://myanimelist.net/anime/genre/41/Suspense?page=1")
    # sample_scraper()

