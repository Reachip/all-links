import pytest
import json
from all_links.website import Website, WebsiteArchitecture


class TestWebsite:
    @pytest.fixture
    def website(self, html_page_title):
        return Website(html_page_title)

    def test__get_absolute_link(self, website):
        link = "/a_test_link"
        assert website._get_absolute_link(link) == f"{str(website)}{link}"
        link = "a_test_link.html"
        assert website._get_absolute_link(link) == f"{str(website)}/{link}"
        link = f"{str(self.website)}/a_test_link"
        assert website._get_absolute_link(link) == link

    def test__link_is_on_website(self, website):
        link = "https://google.fr"
        assert website._link_is_on_website(link) == False

        link = f"{str(website)}/a_test_link"
        assert website._link_is_on_website(link) == True


class TestWebsiteArchitecture:
    @pytest.fixture
    def website_architecture(self, website_links):
        return WebsiteArchitecture(website_links)

    def test_to_json(self, website_architecture, website_links_dict):
        assert website_architecture.to_json() == json.dumps(
            website_links_dict, sort_keys=True, indent=4
        )
