from all_links.parser import HTMLParser
from all_links.request import HTTPRequest
from all_links.writer import FileWriter


class Website:
    def __init__(self, url):
        self.url = url

    def _get_absolute_link(self, link):
        if link.startswith("/"):
            link = self.url + link

        if not link.startswith(self.url) and not link.startswith("http") and link.endswith(".html"):
            link = self.url + "/" + link

        return link

    def _link_is_on_website(self, link):
        return link != self.url and link.startswith(self.url)

    def get_links(self):
        def _get_links(url, links=[]):
            request = HTTPRequest(url)
            request.make_request()
            parser = HTMLParser(request)

            for link in parser.iter_links():
                absolute_link = str(self._get_absolute_link(link))

                if self._link_is_on_website(absolute_link) and absolute_link not in links:
                    links.append(absolute_link)
                    _get_links(absolute_link, links)

            return links

        return _get_links(self.url)

    def __str__(self):
        return self.url
