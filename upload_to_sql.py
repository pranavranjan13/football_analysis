import pandas as pd
import pyodbc

# Load your CSV
df = pd.read_csv('top_players_all_leagues.csv')

# Drop the 'rating' column if it exists
if 'rating' in df.columns:
    df = df.drop(columns=['rating'])

# Clean and convert numeric fields
numeric_columns = ['age', 'appearances', 'minutes', 'goals', 'assists', 'shots', 'shots_on_target', 'key_passes']
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to float; invalids become NaN

# Fill NaN with defaults or leave them for NULL insertion
df = df.fillna(0)

# Connect to SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=playeranalysis;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

# Insert data row by row
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO TopPlayers (
            league, name, age, nationality, team, position, 
            appearances, minutes, goals, assists, shots, 
            shots_on_target, key_passes
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, 
    row['league'], row['name'], row['age'], row['nationality'], row['team'],
    row['position'], row['appearances'], row['minutes'], row['goals'], row['assists'],
    row['shots'], row['shots_on_target'], row['key_passes']
    )

conn.commit()
cursor.close()
conn.close()

print("Upload complete.")
