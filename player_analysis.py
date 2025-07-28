import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your CSV
df = pd.read_csv('top_players_all_leagues.csv')

# Clean and convert numeric columns
numeric_cols = ['age', 'appearances', 'minutes', 'goals', 'assists', 
                'shots', 'shots_on_target', 'key_passes']

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# Calculate new metrics
df['goals_per_90'] = (df['goals'] / df['minutes']) * 90
df['assists_per_90'] = (df['assists'] / df['minutes']) * 90
df['shots_accuracy'] = df['shots_on_target'] / df['shots'].replace(0, 1)  # avoid div by zero
df['key_passes_per_appearance'] = df['key_passes'] / df['appearances'].replace(0, 1)

# Top 10 players by goals per 90
top_goals = df.sort_values('goals_per_90', ascending=False).head(10)

# Plot Top 10 goals per 90
plt.figure(figsize=(12,6))
sns.barplot(x='name', y='goals_per_90', data=top_goals)
plt.xticks(rotation=45)
plt.title('Top 10 Players by Goals per 90 Minutes')
plt.ylabel('Goals per 90')
plt.xlabel('Player Name')
plt.show()

# Plot shots accuracy distribution
plt.figure(figsize=(8,5))
sns.histplot(df['shots_accuracy'], bins=20, kde=True)
plt.title('Distribution of Shots Accuracy')
plt.xlabel('Shots Accuracy')
plt.ylabel('Number of Players')
plt.show()

# Scatter plot: Key Passes vs Assists
plt.figure(figsize=(10,6))
sns.scatterplot(x='key_passes_per_appearance', y='assists_per_90', data=df)
plt.title('Key Passes per Appearance vs Assists per 90')
plt.xlabel('Key Passes per Appearance')
plt.ylabel('Assists per 90 Minutes')
plt.show()
