import elo
import urllib
from sleeper_interface import Sleeper


# 2020ID: 515554164748345344

class TheShow:
    def __init__(self):
        the_show = Sleeper(474716983871401984)
        the_show.get_matchup_data(5)
        print(the_show.league.get_users()[1]['display_name']) # display the name of team1
        print(the_show.league.get_users()[1])

        print(the_show.league.get_matchups(1))

    def get_data(self):
        pass


    def calc_elo(self):
        pass


def main():
    the_show = TheShow()

if __name__ == '__main__':
    main()
