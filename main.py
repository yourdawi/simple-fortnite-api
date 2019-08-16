# yourdawi.de / github.com/yourdawi

import requests
import json
import os

authkey = False
PlayerOne = None

if os.path.isfile("apikey.txt"):
    f = open("apikey.txt", "r")
    authkey = str(f.read())
    print("Loading API Key found in apikey.txt: " + authkey)
else:
    authkey = input("Please enter your API Key. Avaible at fortniteapi.com\n")
    saveAPIkey = input("Do you want to save it? Type yes/no\n")
    if saveAPIkey == "yes":
        f = open("apikey.txt", "w+")
        f.write(authkey)
        f.close()
        print("Loading API Key: " + authkey)
    else:
        print("Loading API Key: " + authkey)


class APIConnect:
    payload = {}
    headers = {
        'Authorization': authkey
    }


class User:

    def __init__(self, nickname, uid, platform):
        print("USER LOADED")

        self.Nickname = nickname
        self.UserID = uid
        self.Platform = platform

        self.StatsAPI = "https://fortnite-api.theapinetwork.com/prod09/users/public/br_stats?user_id=" + self.UserID + "&platform=" + self.Platform
        self.Receive = requests.request('GET', self.StatsAPI, headers=APIConnect.headers, data=APIConnect.payload,
                                        allow_redirects=False)
        self.StatsResult = json.loads(self.Receive.text)

        self.Solo = Solo(self.StatsResult)
        self.Duo = Duo(self.StatsResult)
        self.Squad = Squad(self.StatsResult)
        self.Total = Total(self.StatsResult)

class Solo:

    def __init__(self, statsresult):
        self.StatsResult = statsresult

        self.Kills = self.StatsResult["stats"]["kills_solo"]

        self.Top1 = self.StatsResult["stats"]["placetop1_solo"]

        self.Top2 = self.StatsResult["stats"]["placetop10_solo"]

        self.Top3 = self.StatsResult["stats"]["placetop25_solo"]

        self.MatchesPlayed = self.StatsResult["stats"]["matchesplayed_solo"]

        self.KD = self.StatsResult["stats"]["kd_solo"]

        self.Winrate = self.StatsResult["stats"]["winrate_solo"]

        self.Score = self.StatsResult["stats"]["score_solo"]

    def getKills(self):
        return self.Kills

    def getTop1(self):
        return self.Top1, "Top 1"

    def getTop2(self):
        return self.Top2, "Top 10"

    def getTop3(self):
        return self.Top3, "Top 25"

    def getMatchesPlayed(self):
        return self.MatchesPlayed

    def getKD(self):
        return self.KD

    def getWinRate(self):
        return self.Winrate

    def getScore(self):
        return self.Score


class Duo:

    def __init__(self, statsresult):
        self.StatsResult = statsresult

        self.Kills = self.StatsResult["stats"]["kills_duo"]

        self.Top1 = self.StatsResult["stats"]["placetop1_duo"]

        self.Top2 = self.StatsResult["stats"]["placetop5_duo"]

        self.Top3 = self.StatsResult["stats"]["placetop12_duo"]

        self.MatchesPlayed = self.StatsResult["stats"]["matchesplayed_duo"]

        self.KD = self.StatsResult["stats"]["kd_duo"]

        self.Winrate = self.StatsResult["stats"]["winrate_duo"]

        self.Score = self.StatsResult["stats"]["score_duo"]

    def getKills(self):
        return self.Kills

    def getTop1(self):
        return self.Top1, "Top 1"

    def getTop2(self):
        return self.Top2, "Top 5"

    def getTop3(self):
        return self.Top3, "Top 12"

    def getMatchesPlayed(self):
        return self.MatchesPlayed

    def getKD(self):
        return self.KD

    def getWinRate(self):
        return self.Winrate

    def getScore(self):
        return self.Score


class Squad:
    def __init__(self, statsresult):
        self.StatsResult = statsresult

        self.Kills = self.StatsResult["stats"]["kills_squad"]

        self.Top1 = self.StatsResult["stats"]["placetop1_squad"]

        self.Top2 = self.StatsResult["stats"]["placetop3_squad"]

        self.Top3 = self.StatsResult["stats"]["placetop6_squad"]

        self.MatchesPlayed = self.StatsResult["stats"]["matchesplayed_squad"]

        self.KD = self.StatsResult["stats"]["kd_squad"]

        self.Winrate = self.StatsResult["stats"]["winrate_squad"]

        self.Score = self.StatsResult["stats"]["score_squad"]

    def getKills(self):
        return self.Kills

    def getTop1(self):
        return self.Top1, "Top 1"

    def getTop2(self):
        return self.Top2, "Top 3"

    def getTop3(self):
        return self.Top3, "Top 6"

    def getMatchesPlayed(self):
        return self.MatchesPlayed

    def getKD(self):
        return self.KD

    def getWinRate(self):
        return self.Winrate

    def getScore(self):
        return self.Score


class Total:

    def __init__(self, statsresult):

        self.StatsResult = statsresult

        self.Kills = self.StatsResult["totals"]["kills"]

        self.Wins = self.StatsResult["totals"]["wins"]

        self.MatchesPlayed = self.StatsResult["totals"]["matchesplayed"]

        self.Score = self.StatsResult["totals"]["score"]

        self.Winrate = self.StatsResult["totals"]["winrate"]

        self.KD = self.StatsResult["totals"]["kd"]

    def getKills(self):
        return self.Kills

    def getWins(self):
        return self.Wins

    def getMatchesPlayed(self):
        return self.MatchesPlayed

    def getScore(self):
        return self.Score

    def getWinRate(self):
        return self.Winrate

    def getKD(self):
        return self.KD


def updateAPI():
    pass


def GetUser():
    nickname = input("Please enter a username:\n")
    print("Receiving data from user : " + nickname + "\n")
    iplatform = input("Please select a platform. pc, ps4 or xbox\n Default: ps4\n")
    iplatform = str.lower(iplatform)
    if iplatform == "pc" or iplatform == "ps4" or iplatform == "xbox":
        platform = iplatform
    else:
        platform = "ps4"

    userid = "https://fortnite-api.theapinetwork.com/users/id?username=" + nickname
    getIt = requests.request('GET', userid, headers=APIConnect.headers, data=APIConnect.payload,
                             allow_redirects=False, )
    getItJson = json.loads(getIt.text)

    try:
        getItJson["data"]["uid"]
        uid = getItJson["data"]["uid"]
        global PlayerOne
        PlayerOne = User(nickname, uid, platform)
        print(PlayerOne)
    except KeyError:
        GetUser()
        return False


GetUser()
