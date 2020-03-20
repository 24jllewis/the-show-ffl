import requests
from sleeper_wrapper import League, User, Stats, Drafts, Players
# the Show leagueID: 474716983871401984

class Sleeper:
    def __init__(self, league_id):
        self.league_id = str(league_id)
        self.league = League(self.league_id)

        # print(my_league.get_matchups(5)[5])

    def get_matchup_data(self, week):
        '''

        :param week: Week for which matchups will be retrieved
        :return:
        '''
        week = str(week)
        # GET
        # https: // api.sleeper.app / v1 / league / < league_id > / matchups / < week >
        matchup_data = requests.get("https://api.sleeper.app/v1/league/" + self.league_id + "/matchups/" + week).json()
        print(matchup_data[5])
