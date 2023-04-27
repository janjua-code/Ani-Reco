from typing import Optional


class Entry:
    """
    An abstract class for a show entry.

    ===Attributes===
    title: The name/title of the media
    link: Link to the entry on a database
    rating: Rating of the show (None if rating is not available)
    popularity: Popularity of the show
    tags: List of all the Genre/themes associated with the show
    recommendations: List of all show recommendations for this show

    ===Representation Invariants===
    recommendations are always sorted from most to least recommended
    """
    title: str
    link: str
    rating: Optional[float]
    popularity: int
    tags: list[str]
    recommendations: list[str]

    def __init__(self, title: str, link: str, rating: Optional[float],
                 popularity: int, tags: list[str],
                 recommendations: list[str]) -> None:
        """Initialize an entry with <title>, <link>, <rating>, <popularity>,
        <tags>, and <recommendations>"""
        self.title = title
        self.link = link
        self.rating = rating
        self.popularity = popularity
        self.tags = tags
        self.recommendations = recommendations


class AnimeEntry(Entry):
    """
    A subclass of Entry for an anime entry

    ===Attributes===
    title: The name/title of the media
    link: Link to the entry on a database
    rating: Rating of the show (None if rating is not available)
    popularity: Popularity of the show
    tags: List of all the Genre/themes associated with the show
    recommendations: List of all show recommendations for this show

    ===Representation Invariants===
    recommendations are always sorted from most to least recommended
    """
    title: str
    link: str
    rating: Optional[float]
    popularity: int
    tags: list[str]
    recommendations: list[str]

    def __init__(self, title: str, link: str, rating: Optional[float],
                 popularity: int, tags: list[str],
                 recommendations: list[str]) -> None:
        """Initializer inherits from Entry"""
        Entry.__init__(self, title, link, rating, popularity, tags,
                       recommendations)

    def __str__(self) -> str:
        """Represent the anime entry in string format
        >>> anime = AnimeEntry("Naruto", \
        "https://myanimelist.net/anime/20/Naruto", 7.98, 8,\
        ["Shounen", "Action", "Fantasy"], ["Black Clover", "One Piece"])
        >>> print(anime)
        Naruto
        https://myanimelist.net/anime/20/Naruto
        7.98
        8
        Shounen, Action, Fantasy
        Black Clover, One Piece
        """
        s = self.title + "\n" + self.link + "\n" + str(self.rating) + "\n" + \
            str(self.popularity) + "\n"
        t = ""
        for tag in self.tags:
            if t == "":
                t = tag
            else:
                t = t + ", " + tag
        r = ""
        for reco in self.recommendations:
            if r == "":
                r = reco
            else:
                r = r + ", " + reco
        return s + t + "\n" + r
