from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or
from query_builder import QueryBuilder

def spacer():
    print ("--")

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    m1 = (
      query
        .playsIn("PHI")
        .hasAtLeast(10, "assists")
        .hasFewerThan(5, "goals")
        .build()
    )

    m2 = (
      query
        .playsIn("EDM")
        .hasAtLeast(50, "points")
        .build()
    )

    matcher = query.oneOf(m1, m2).build() 

    for player in stats.matches(matcher):
        print(player)

    #matcher = query.build()
    #matcher = query.playsIn("NYR").hasAtLeast(10, "goals").hasFewerThan(20, "goals").build()

    #for player in stats.matches(matcher):
        #print(player)

    #matcher = And(
        #HasAtLeast(5, "goals"),
        #HasAtLeast(5, "assists"),
        #PlaysIn("PHI")
    #)
#
    #for player in stats.matches(matcher):
        #print(player)
#
    #spacer()
#
    #matcher = And(
        #Not(HasAtLeast(1, "goals")),
        #PlaysIn("NYR")
    #)
#
    #for player in stats.matches(matcher):
        #print(player)
#
    #spacer()
    #
    #matcher = And(
        #HasFewerThan(1, "goals"),
        #PlaysIn("NYR")
    #)
#
    #for player in stats.matches(matcher):
        #print(player)
#
    #spacer()
    #
    #filtered_with_all = stats.matches(All())
    #print(len(filtered_with_all))
#
    #spacer()
    #
    #matcher = Or(
        #HasAtLeast(45, "goals"),
        #HasAtLeast(70, "assists")
    #)
#
    #for player in stats.matches(matcher):
        #print(player)
#
    #spacer()
    #
    #matcher = And(
        #HasAtLeast(70, "points"),
        #Or(
            #PlaysIn("NYR"),
            #PlaysIn("FLA"),
            #PlaysIn("BOS")
        #)
    #)
#
    #for player in stats.matches(matcher):
        #print(player)

if __name__ == "__main__":
    main()
