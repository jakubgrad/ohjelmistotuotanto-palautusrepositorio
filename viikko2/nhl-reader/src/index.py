from player_reader import PlayerReader
from player_stats import PlayerStats
from rich import print
from rich.table import Table
from rich.prompt import Prompt

def display_top_scorers(players, nationality, season):
    table = Table(title=f"Top scorers of {nationality} season {season}")
    table.add_column("name")
    table.add_column("team")
    table.add_column("goals")
    table.add_column("assists")
    table.add_column("points")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

    print(table)

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    season = Prompt.ask("Select season [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25]").strip()

    while True:
        nationality = Prompt.ask("Select nationality [AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR]").strip().upper()
        
        players = stats.top_scorers_by_nationality(nationality)
        display_top_scorers(players, nationality, season)

if __name__ == "__main__":
    main()
