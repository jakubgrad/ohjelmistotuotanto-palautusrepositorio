from statistics_service import StatisticsService, SortBy
from player_reader import PlayerReader 


def main():
    stats = StatisticsService(
      PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt")
    )
    
     # järjestetään pisteiden perusteella, parametrina oleva 1 määrää järjestyksen
    for player in stats.top(10, 1):
        print(player)

    # järjestetään syöttöjen perusteella, parametrina oleva 3 määrää järjestyksen
    print("Top by assists:")
    for player in stats.top(10, 3):
        print(player)

    print("Top point getters:")
    for player in stats.top(10, SortBy.POINTS):
        print(player)
    print("")

    # metodi toimii samalla tavalla kuin yo. kutsu myös ilman toista parametria
    for player in stats.top(10):
        print(player)

    # järjestetään maalien perusteella
    print("Top point goal scorers:")
    for player in stats.top(10, SortBy.GOALS):
        print(player)
    print("")

if __name__ == "__main__":
    main()
