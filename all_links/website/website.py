import uuid
from parser import HTMLParser
from request import HTTPRequest
from writer import FileWriter
from cache import Cache


class Website:
    def __init__(self, url):
        self.url = url
        self._id = str(uuid.uuid4())

    def _get_absolute_link(self, link):
        if link.startswith("/"):
            link = self.url + link

        if (
            not link.startswith(self.url)
            and not link.startswith("http")
            and link.endswith(".html")
        ):
            link = self.url + "/" + link

        return link

    def _link_is_on_website(self, link):
        return link != self.url and link.startswith(self.url)

    def get_links(self):
        def _get_links(url):
            with Cache(self._id) as cache:
                request = HTTPRequest(url)
                request.make_request()
                parser = HTMLParser(request)

                for link in parser.iter_links():
                    absolute_link = str(self._get_absolute_link(link))

                    link_is_on_website = self._link_is_on_website(absolute_link)
                    link_is_on_the_cache = cache.link_is_on_the_cache(absolute_link)

                    if link_is_on_website and not link_is_on_the_cache:
                        cache.store_link(absolute_link)
                        _get_links(absolute_link)

                return cache.get_links()

        return _get_links(self.url)

    def __str__(self):
        return self.url
