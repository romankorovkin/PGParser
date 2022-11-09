from platform import release
from bs4 import BeautifulSoup

class PageGameParser():

    def __init__(self, html: str):
        self.bs = BeautifulSoup(html, "lxml")

    def getName(self):
        block = self.bs.find("h1", class_ = "gp-game-title")
        name = block.next_element.lstrip(" \n").rstrip(" \n")
        return name

    def getReleases(self):
        release_items = self.bs.find_all("div", class_ = "release-item")
        releases = {}
        for release_item in release_items:
            platform = release_item.a.extract().get_text().replace("\n", "").replace(" ", "")
            date = release_item.get_text().replace("\n", "").replace(" ", "")
            releases[platform] = date
        return releases

    def getDescription(self):
        description = self.bs.find("div", class_ = "description-wrapper")
        if description == None:
            return None
        return description.get_text()