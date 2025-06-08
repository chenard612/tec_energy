from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from app.parser import parse_csv_file

BASE_URL = "https://twtransfer.energytransfer.com/ipost/TW/capacity/operationally-available"

def query_csv():
    response = requests.get(BASE_URL)

    if response.status_code != 200:
        print(f"[{date.date()}] Failed to load HTML page")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    menu_spans = soup.find_all("span", class_="menuButton")

    csv_url = None
    for span in menu_spans:
        link = span.find("a", class_="csv")
        if link and "csv" in link["href"]:
            relative_csv_link = link["href"]
            csv_url = urljoin(BASE_URL, relative_csv_link)
            break

    if not csv_url:
        print(f"CSV link not found")
        return

    csv_response = requests.get(csv_url)


    if csv_response.status_code == 200:
        print(f"[Downloaded CSV successfully]")
        parse_csv_file(csv_response.text)
    else:
        print(f"Failed to download for {date.date()}")
        return