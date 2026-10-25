"""Jednostavan primjer web scrapinga uz requests i BeautifulSoup."""

import requests
from bs4 import BeautifulSoup

URL = "https://www.index.hr/"

try:
    response = requests.get(URL, timeout=15)
    response.raise_for_status()
except requests.RequestException as error:
    print(f"Stranicu nije moguće preuzeti: {error}")
else:
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.get_text(strip=True) if soup.title else "(stranica nema naslov)"
    print(f"Naslov stranice: {title}\n")

    quotes = soup.select(".quote")
    if not quotes:
        print("Na stranici nisu pronađeni citati.")

    for number, quote in enumerate(quotes, start=1):
        text = quote.select_one(".text")
        author = quote.select_one(".author")

        quote_text = text.get_text(strip=True) if text else "(nema teksta)"
        quote_author = author.get_text(strip=True) if author else "Nepoznat autor"
        print(f"{number}. {quote_text} — {quote_author}")
