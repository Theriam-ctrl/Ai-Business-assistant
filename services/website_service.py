import re
import requests

from bs4 import BeautifulSoup

from services.crawler_service import (
    find_important_links
)


def clean_page(html):

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    for tag in soup(
        [
            "script",
            "style",
            "noscript",
            "svg",
            "footer"
        ]
    ):
        tag.decompose()

    return soup.get_text(
        separator="\n",
        strip=True
    )


def download_page(url):

    response = requests.get(
        url,
        timeout=15,
        headers={
            "User-Agent":
            "Theriam AI Receptionist"
        }
    )

    response.raise_for_status()

    return response.text


def fetch_website(url):

    try:

        if not url.startswith(
            (
                "http://",
                "https://"
            )
        ):
            url = "https://" + url

        homepage_html = download_page(url)

        soup = BeautifulSoup(
            homepage_html,
            "html.parser"
        )

        title = ""

        if soup.title:
            title = soup.title.get_text(
                strip=True
            )

        combined_text = clean_page(
            homepage_html
        )

        links = find_important_links(
            url
        )

        pages_read = 1

        for page_name, page_url in links.items():

            try:

                html = download_page(
                    page_url
                )

                combined_text += (
                    "\n\n"
                    + clean_page(html)
                )

                pages_read += 1

            except Exception:

                pass

        email_match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            combined_text
        )

        phone_match = re.search(
            r"(\+?\d[\d\s\-\(\)]{7,}\d)",
            combined_text
        )

        return {

            "success": True,

            "url": url,

            "title": title,

            "email":
                email_match.group(0)
                if email_match
                else "",

            "phone":
                phone_match.group(0)
                if phone_match
                else "",

            "pages_read": pages_read,

            "pages_found": list(
                links.keys()
            ),

            "text": combined_text

        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)

        }