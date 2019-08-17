# yourdawi.de / github.com/yourdawi

from main import *
from PIL import Image
import io
from datetime import datetime


def switchMode():
    mode = input("1 - Stats\n2 - News\n3- Weapon\n")
    if mode == "1":
        StatsMode = input("Solo, Duo, Squad or total?\n")
        StatsMode = StatsMode.capitalize()

        if StatsMode == "Solo" or StatsMode == "Duo" or StatsMode == "Squad":
            if StatsMode == "Solo":
                Amode = PlayerOne.Solo
            if StatsMode == "Duo":
                Amode = PlayerOne.Duo
            if StatsMode == "Squad":
                Amode = PlayerOne.Squad

            print("+++++ " + StatsMode + " stats for user " + PlayerOne.Nickname + " +++++")
            print("Kills: " + str(Amode.getKills()))
            placeA, textA = Amode.getTop1()
            print(textA + ": " + str(placeA))
            placeB, textB = Amode.getTop2()
            print(textB + ": " + str(placeB))
            placeC, textC = Amode.getTop3()
            print(textC + ": " + str(placeC))
            print("Winrate: " + str(Amode.getWinRate()))
            print("Score: " + str(Amode.getScore()))
            print("Matches played: " + str(Amode.getMatchesPlayed()))
            print("Last update: " + str(datetime.fromtimestamp(Amode.getLastUpdate())))

            switchMode()
        elif StatsMode == "Total":
            Amode = PlayerOne.Total

            print("+++++ " + StatsMode + " stats for user " + PlayerOne.Nickname + " +++++")
            print("Kills: " + str(Amode.getKills()))
            print("Wins: " + str(Amode.getWins()))
            print("Winrate: " + str(Amode.getWinRate()))
            print("Score: " + str(Amode.getScore()))
            print("Matches played: " + str(Amode.getMatchesPlayed()))

            switchMode()

        else:
            print("Please select Solo, Duo, Squad or Total!")
            switchMode()
            return False
    elif mode == "2":
        print(News.NewsBR["data"][0]["title"])
        print(News.NewsBR["data"][0]["body"])

        """ THIS IS TO SHOW THE IMAGE
        imgResponse = requests.get(News.NewsBR["data"][0]["image"])
        i = Image.open(io.BytesIO(imgResponse.content))
        i.show()"""
        switchMode()
    elif mode == "3":
        i = 0
        while i < len(Weapon.WeaponList["data"]["entries"]):
            if Weapon.WeaponList["data"]["entries"][i]["vaulted"] == 0:
                print(Weapon.WeaponList["data"]["entries"][i]["name"] + " - " + Weapon.WeaponList["data"]["entries"][i]["rarity"])
            else:
                print("VAULTED: " + Weapon.WeaponList["data"]["entries"][i]["name"] + " - " +
                      Weapon.WeaponList["data"]["entries"][i]["rarity"])

            i += 1

        switchMode()

    else:
        print("Incorrect input!")
        switchMode()
        return False


switchMode()
