import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin


KEYWORDS = [
    "contact",
    "about",
    "service",
    "faq",
    "pricing",
    "products"
]


def find_important_links(base_url):

    try:

        response = requests.get(
            base_url,
            timeout=15,
            headers={
                "User-Agent": "Theriam AI Receptionist"
            }
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        links = {}

        for link in soup.find_all("a", href=True):

            href = link["href"]

            text = link.get_text(
                strip=True
            ).lower()

            full_url = urljoin(
                base_url,
                href
            )

            for keyword in KEYWORDS:

                if (
                    keyword in text
                    or keyword in href.lower()
                ):

                    links[keyword] = full_url

        return links

    except Exception:

        return {}