from typing import Optional


class Entry:
    """
    An abstract class for a show entry
    ===Attributes===
    title: The name/title of the media
    link: Link to the entry on a database
    tags: List of all the Genre/themes associated with the show
    rating: Rating of the show (None if rating is not available)
    recommendations: List of all show recommendations for this show
    """
    title: str
    link: str
    tags: list[str]
    rating: Optional[float]
    recommendations: list[str]

    def __init__(self, title: str, link: str, tags: list[str], rating: Optional[
        float], recommendations: list[str]) -> None:
        """Initialize an entry with <title>, <link>, <tags>, <rating>, and
        <recommendations>"""
        self.title = title
        self.link = link
        self.tags = tags
        self.rating = rating
        self.recommendations = recommendations


class AnimeEntry(Entry):
    """
    A subclass of Entry for an anime entry
    ===Attributes===
    title: The name/title of the anime
    link: Link to the entry on a database (MyAnimeList)
    tags: Genre/themes of the show
    """
    title: str
    link: str
    tags: list[str]

    def __init__(self, title: str, link: str, tags: list[str], rating: float,
                 recommendations: list[str]) -> None:
        """Initializer inherits from Entry"""
        Entry.__init__(self, title, link, tags, rating, recommendations)

    def __str__(self) -> str:
        """Represent the anime entry in string format
        >>> anime = AnimeEntry("Naruto", "https://myanimelist.net/anime/20/Naruto", ["Shounen", "Action", "Fantasy"], 7.98, ["Black Clover", "One Piece"])
        >>> print(anime)
        Naruto
        https://myanimelist.net/anime/20/Naruto
        Shounen, Action, Fantasy
        7.98
        Black Clover, One Piece
        """
        s = self.title + "\n" + self.link + "\n" + str(self.rating) + "\n"
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
