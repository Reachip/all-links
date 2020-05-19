from all_links.request import HTTPRequest
from all_links.website import Website

class TestHTTPRequest:
    website = Website("https://reachip.github.io")
    
    def test_make_request(self, mocker, html):
        class ResponseMocker:
            @property
            def content(self):
                return html

        request_mock = mocker.patch("requests.Session").return_value
        request_mock.get.return_value = ResponseMocker()

        http_req = HTTPRequest(self.website)
        http_req.make_request()

        assert http_req.content == html
