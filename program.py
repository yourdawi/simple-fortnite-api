# yourdawi.de / github.com/yourdawi

from main import *


def switchMode():
    mode = input("Solo, Duo, Squad or total?\n")
    mode = mode.capitalize()

    if mode == "Solo" or mode == "Duo" or mode == "Squad":
        if mode == "Solo":
            Amode = solo
        if mode == "Duo":
            Amode = duo
        if mode == "Squad":
            Amode = squad

        print("+++++ " + mode + " stats for user " + user.Nickname + " +++++")
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

        switchMode()
    elif mode == "Total":
        Amode = total

        print("+++++ " + mode + " stats for user " + user.Nickname + " +++++")
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


switchMode()
