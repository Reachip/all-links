import pytest


@pytest.fixture
def html_page_title():
    return "A page title"


@pytest.fixture
def page_url():
    return "https://reachip.free.fr"


@pytest.fixture
def website_links():
    return (
        "https://b/a/CV.html#CV",
        "https://b/a/tmp.html#tmp",
        "https://b/a/projets-scolaires.html#projets-scolaires",
        "https://b/c/js.html",
        "https://b/c/python.html",
        "https://b/c/programmation.html",
        "https://b/c/quora.html",
        "https://b/c/rust.html",
        "https://b/c/sti2d.html",
        "https://b/"
    )

@pytest.fixture
def website_links_dict():
    return {
        "": [
            "https://b/"
        ],

        "a": [
            "https://b/a/CV.html#CV",
            "https://b/a/tmp.html#tmp",
            "https://b/a/projets-scolaires.html#projets-scolaires",
        ],

        "c": [
            "https://b/c/js.html",
            "https://b/c/python.html",
            "https://b/c/programmation.html",
            "https://b/c/quora.html",
            "https://b/c/rust.html",
            "https://b/c/sti2d.html"
        ]
    }


@pytest.fixture
def page_urls(page_url):
    return (page_url, "/test")


@pytest.fixture
def page_urls_html(page_url):
    return f"""
        <a href="{page_url}"></a>
        <a href="/test"></a>
    """


@pytest.fixture
def html(html_page_title, page_urls_html):
    return f"""
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title>{html_page_title}</title>
            </head>
            <body>
                {page_urls_html}
            </body>
        </html>
    """
