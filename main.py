# yourdawi.de / github.com/yourdawi

import requests
import json
import os

authkey = False
nickname = False
uid = False
platform = "ps4"

if not os.path.isfile("apikey.txt"):
    authkey = input("Please enter your API Key. Avaible at fortniteapi.com\n")
    saveAPIkey = input("Do you want to save it? Type yes/no\n")
    if saveAPIkey == "yes":
        f = open("apikey.txt", "w+")
        f.write(authkey)
        f.close()

f = open("apikey.txt", "r")
authkey = str(f.read())
print("Loading API Key found in apikey.txt: " + authkey)


class APIConnect:
    payload = {}
    headers = {
        'Authorization': authkey
    }


def GetUser():
    global nickname
    nickname = input("Please enter a username:\n")
    print("Receiving data from user : " + nickname + "\n")
    global platform
    iplatform = input("Please select a platform. pc, ps4 or xbox\n Default: ps4\n")
    iplatform = str.lower(iplatform)
    if iplatform == "pc" or iplatform == "ps4" or iplatform == "xbox":
        platform = iplatform

    userid = "https://fortnite-api.theapinetwork.com/users/id?username=" + nickname
    getIt = requests.request('GET', userid, headers=APIConnect.headers, data=APIConnect.payload,
                             allow_redirects=False, )
    getItJson = json.loads(getIt.text)

    try:
        getItJson["data"]["uid"]
        global uid
        uid = getItJson["data"]["uid"]
    except KeyError:
        GetUser()
        return False


while GetUser():
    pass  #


class User:
    Nickname = nickname
    UserID = uid
    Platform = platform

    StatsAPI = "https://fortnite-api.theapinetwork.com/prod09/users/public/br_stats?user_id=" + UserID + "&platform=" + Platform
    receive = requests.request('GET', StatsAPI, headers=APIConnect.headers, data=APIConnect.payload,
                               allow_redirects=False)
    StatsResult = json.loads(receive.text)


user = User()


class Solo:
    kills = User.StatsResult["stats"]["kills_solo"]

    def getKills(self):
        return self.kills

    placetop1 = User.StatsResult["stats"]["placetop1_solo"]

    def getTop1(self):
        return self.placetop1, "Top 1"

    placetop10 = User.StatsResult["stats"]["placetop10_solo"]

    def getTop2(self):
        return self.placetop10, "Top 10"

    placetop25 = User.StatsResult["stats"]["placetop25_solo"]

    def getTop3(self):
        return self.placetop25, "Top 25"

    matchesplayed = User.StatsResult["stats"]["matchesplayed_solo"]

    def getMatchesPlayed(self):
        return self.matchesplayed

    kd = User.StatsResult["stats"]["kd_solo"]

    def getKD(self):
        return self.kd

    winrate = User.StatsResult["stats"]["winrate_solo"]

    def getWinRate(self):
        return self.winrate

    score = User.StatsResult["stats"]["score_solo"]

    def getScore(self):
        return self.score


solo = Solo()


class Duo:
    kills = User.StatsResult["stats"]["kills_duo"]

    def getKills(self):
        return self.kills

    placetop1 = User.StatsResult["stats"]["placetop1_duo"]

    def getTop1(self):
        return self.placetop1, "Top 1"

    placetop5 = User.StatsResult["stats"]["placetop5_duo"]

    def getTop2(self):
        return self.placetop5, "Top 5"

    placetop12 = User.StatsResult["stats"]["placetop12_duo"]

    def getTop3(self):
        return self.placetop12, "Top 12"

    matchesplayed = User.StatsResult["stats"]["matchesplayed_duo"]

    def getMatchesPlayed(self):
        return self.matchesplayed

    kd = User.StatsResult["stats"]["kd_duo"]

    def getKD(self):
        return self.kd

    winrate = User.StatsResult["stats"]["winrate_duo"]

    def getWinRate(self):
        return self.winrate

    score = User.StatsResult["stats"]["score_duo"]

    def getScore(self):
        return self.score


duo = Duo()


class Squad:
    kills = User.StatsResult["stats"]["kills_squad"]

    def getKills(self):
        return self.kills

    placetop1 = User.StatsResult["stats"]["placetop1_squad"]

    def getTop1(self):
        return self.placetop1, "Top 1"

    placetop3 = User.StatsResult["stats"]["placetop3_squad"]

    def getTop2(self):
        return self.placetop3, "Top 3"

    placetop6 = User.StatsResult["stats"]["placetop6_squad"]

    def getTop3(self):
        return self.placetop6, "Top 6"

    matchesplayed = User.StatsResult["stats"]["matchesplayed_squad"]

    def getMatchesPlayed(self):
        return self.matchesplayed

    kd = User.StatsResult["stats"]["kd_squad"]

    def getKD(self):
        return self.kd

    winrate = User.StatsResult["stats"]["winrate_squad"]

    def getWinRate(self):
        return self.winrate

    score = User.StatsResult["stats"]["score_squad"]

    def getScore(self):
        return self.score


squad = Squad()


class Total:
    kills = User.StatsResult["totals"]["kills"]

    def getKills(self):
        return self.kills

    wins = User.StatsResult["totals"]["wins"]

    def getWins(self):
        return self.wins

    matchesplayed = User.StatsResult["totals"]["matchesplayed"]

    def getMatchesPlayed(self):
        return self.matchesplayed

    score = User.StatsResult["totals"]["score"]

    def getScore(self):
        return self.score

    winrate = User.StatsResult["totals"]["winrate"]

    def getWinRate(self):
        return self.winrate

    kd = User.StatsResult["totals"]["kd"]

    def getKD(self):
        return self.kd


total = Total()
