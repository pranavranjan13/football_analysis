# Soccer Player Performance Analysis

This project involves fetching soccer player performance data from API-Football, cleaning and uploading the data to a SQL Server database, and performing analysis to derive meaningful insights.

## Project Overview

- **Data Source:** API-Football
- **Technologies Used:** Python, SQL Server, pandas, pyodbc
- **Goals:**
  - Extract player stats from multiple leagues using API-Football
  - Clean and transform data for analysis
  - Upload cleaned data into SQL Server
  - Analyze player performance metrics such as goals, assists, shots, and minutes played

## Project Structure

- `top_scores.py` — Script to pull player performance data from API-Football
- `upload_to_sql.py` — Script to upload cleaned player data to SQL Server
- `top_players_all_leagues.csv` — Sample dataset containing player stats
- `README.md` — This documentation file

## Getting Started

### Prerequisites

- Python 3.x
- Libraries: `requests`, `pandas`, `pyodbc`, `beautifulsoup4` (if scraping is needed)
- SQL Server instance
- API-Football account and API key
