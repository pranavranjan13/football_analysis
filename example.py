import requests
from bs4 import BeautifulSoup
import urllib.parse

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

def search_player_on_transfermarkt(player_name):
    query = urllib.parse.quote(player_name)
    search_url = f"https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query={query}"

    response = requests.get(search_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find first player result link
    player_link_tag = soup.select_one('a.spielprofil_tooltip')

    if player_link_tag:
        player_relative_url = player_link_tag['href']
        full_url = "https://www.transfermarkt.com" + player_relative_url
        return full_url
    else:
        print(f"No player found for '{player_name}' on Transfermarkt.")
        return None

def get_market_value(player_url):
    response = requests.get(player_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    # Market value is often in the div with class "marktwert"
    marktwert_div = soup.find("div", class_="marktwert")

    if marktwert_div:
        value_span = marktwert_div.find("a")
        if value_span:
            return value_span.text.strip()
    else:
        # Sometimes it may be in other places; fallback attempt:
        table = soup.find("table", class_="auflistung")
        if table:
            for row in table.find_all("tr"):
                if "Market value" in row.text:
                    return row.find_all("td")[1].text.strip()

    return "Market value not found"

# Example usage:
player_name = "Yamal"
player_url = search_player_on_transfermarkt(player_name)

if player_url:
    print(f"Player profile URL: {player_url}")
    market_value = get_market_value(player_url)
    print(f"Market value of {player_name}: {market_value}")
else:
    print("Player not found.")
