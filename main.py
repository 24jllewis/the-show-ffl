
import urllib
from sleeper_interface import Sleeper


class TheShow:
    def __init__(self):
        sleep = Sleeper()
        sleep.get_matchup_data(6)

    def get_data(self):
        pass


def main():
    the_show = TheShow()


if __name__ == '__main__':
    main()
