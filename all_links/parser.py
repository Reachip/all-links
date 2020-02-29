from bs4 import BeautifulSoup


class HTMLParser:
    def __init__(self, html):
        self.html = str(html)
        self.parser = BeautifulSoup(self.html, 'lxml')

    @property
    def page_title(self):
        return str(self.parser.title.string)

    def iter_links(self):
        for a in self.parser.find_all("a"):
            href = str(a.get("href"))

            if href.startswith("http") or href.startswith("/"):
                yield href

    def __str__(self):
        return self.html
