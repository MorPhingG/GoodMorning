import dota2api
import json
import time

class GetDotaData:
    def get(accountId):
        api = dota2api.Initialise("3696FD54789FF3D37C752351029AD9D9")
        match = api.get_match_history(account_id = accountId)
        matchData = json.loads(match.json)
        matchList = []
        heroId = []
        heroName = []
        playerSlot = []
        for i in range(30):
            matchTime = matchData['matches'][i]['start_time']
            matchId = matchData['matches'][i]['match_id']
            player = matchData['matches'][i]['players']
            nowTime = time.time()
            if nowTime - matchTime < 86400:
                matchList.append(matchId)
                heroes = api.get_heroes()
                for j in range(10):
                    if player[j]['account_id'] == accountId:
                        heroId.append(player[j]['hero_id'])
                        n = 0
                        while heroes['heroes'][n]['id'] != player[j]['hero_id']:
                            n = n+1
                        heroName.append(heroes['heroes'][n]['localized_name'])
                        playerSlot.append(player[j]['player_slot'])
                        break

        matchNumber = len(matchList)
        winNumber = 0
        lostNumber = 0
        for i in range(matchNumber):
            matchDetail = api.get_match_details(match_id=matchList[i])
            radiantWin = matchDetail['radiant_win']
            if playerSlot[i] >> 7 == radiantWin:
                lostNumber += 1
            else:
                winNumber += 1
        return heroName, winNumber, lostNumber





