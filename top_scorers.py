import requests
import pandas as pd
import time

API_KEY = 'c2c5d09a056c4817e8b33004b2152de8'
headers = {'x-apisports-key': API_KEY}

# Define leagues and season
leagues = {
    39: "Premier League",
    140: "La Liga",
    135: "Serie A",
    78: "Bundesliga",
    61: "Ligue 1"
}
season = 2023

players_all = []

for league_id, league_name in leagues.items():
    print(f"Fetching data for {league_name}...")

    url = f'https://v3.football.api-sports.io/players/topscorers?league={league_id}&season={season}'
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch data for {league_name}: {response.text}")
        continue

    data = response.json()

    for item in data['response']:
        player = item['player']
        stats = item['statistics'][0]

        players_all.append({
            'league': league_name,
            'name': player['name'],
            'age': player['age'],
            'nationality': player['nationality'],
            'team': stats['team']['name'],
            'position': stats['games']['position'],
            'appearances': stats['games']['appearences'],
            'minutes': stats['games']['minutes'],
            'goals': stats['goals']['total'],
            'assists': stats['goals']['assists'],
            'shots': stats['shots']['total'],
            'shots_on_target': stats['shots']['on'],
            'key_passes': stats['passes']['key'],
            'rating': player.get('rating', None)
        })

    time.sleep(1)  # Pause to avoid hitting rate limit

df = pd.DataFrame(players_all)
df.to_csv('top_players_all_leagues.csv', index=False)
print("✅ Data saved to 'top_players_all_leagues.csv'")
