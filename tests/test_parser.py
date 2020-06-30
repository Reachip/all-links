import pytest
from all_links.parser import HTMLParser

class TestParser:
    @pytest.fixture
    def parser(self, html):
        return HTMLParser(html)

    def test_page_title(self, parser, html_page_title):
        assert parser.page_title == html_page_title

    def test_iter_links(self, parser, page_urls):
        links = parser.iter_links()
        assert tuple(links) == page_urls

    def test___str__(self, parser, html):
        assert str(parser) == html
