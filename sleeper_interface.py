import requests
# leagueID: 474716983871401984

league_id = 474716983871401984

class Sleeper:
    def __init__(self):
        global league_id
        league_id = str(league_id)

    def get_matchup_data(self, week):
        '''

        :param week: Week for which matchups will be retrieved
        :return:
        '''
        week = str(week)
        # GET
        # https: // api.sleeper.app / v1 / league / < league_id > / matchups / < week >
        matchup_data = requests.get("https://api.sleeper.app/v1/league/" + league_id + "/matchups/" + week).json()
        print(matchup_data[5])
