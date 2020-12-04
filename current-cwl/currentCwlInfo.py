#
# This script dumps/prints the enemy TH distribution for the specified clans.
# This has to be run _during_ CWL, after enemies are idenfitied. 
# Supercell does not publish historical data for CWLs.
#

from pyclashofclans import Players
from pyclashofclans import ClanWarLeagues
from collections import defaultdict
from collections import OrderedDict

#
# print TH distribution
# returns a map of (clanTag, map of (TH level, count)) 
#
def printEnemiesTHDistribution(inputTag, cwlData):
    clanToTHLevels = {}
    for clan in cwlData["clans"]:
        # Skip the specified clan
        # The endswith() let us not worry about whether the tag
        # starts with the hash or not. I.e: #12345 or 12345 should
        # work
        if clan["tag"].endswith(inputTag):
            continue
        clanTHLevels = defaultdict(int)
        for member in clan["members"]:
            player = playersApi.find(member["tag"])
            clanTHLevels[player["townHallLevel"]] += 1
        clanToTHLevels[clan["tag"]] = clanTHLevels
        print(clan["name"] + "(" + clan["tag"] + "): ", end='')
        print(dict(sorted(clanTHLevels.items(), key=lambda x: x[0], reverse=True)))
    return clanToTHLevels
    
#
# print rounds
#
def printRounds(inputTag, cwlData, clanToTHLevels):
    num=1
    for round in cwlData["rounds"]:
        for wartag in round["warTags"]:
            if wartag == "#0":
                print("Round {} has not started yet".format(num))
                break
            a_war = cwlApi.get_wartag(wartag)
            clan1 = a_war["clan"]
            clan2 = a_war["opponent"]
            if not clan1["tag"].endswith(inputTag) and not clan2["tag"].endswith(inputTag):
                # not our war
                continue
        
            enemy = clan1
            us = clan2
            if clan1["tag"].endswith(inputTag):
                enemy = clan2
                us = clan1
            print("R{} ({}) ".format(num, wartag), end='')
            print(enemy["name"] + " [" + enemy["tag"] + "]: ", end='')
            print(dict(sorted(clanToTHLevels[enemy["tag"]].items(), key=lambda x: x[0], reverse=True)), end='')
            print(", Stars (us vs them): {} vs {}".format(us["stars"], enemy["stars"]))
            break
        num += 1

#
# MAIN
#

# INPUT: put your API token here, inside of the quotes
apiToken = ""

# INPUT: list the clans you want to get CWL info for
#        First string is the Clan code
#        Second string is the Clan name
inputClans = { 
               "2PPGUPYPG": "Clan Name",
               "2YVJLQLCY": "Clan name"
             }

playersApi = Players(apiToken)
cwlApi = ClanWarLeagues(apiToken)

for clanTag, clanName in inputClans.items():
    print(clanName + ":")
    print("====================")
    cwlData = cwlApi.get_current_leaguegroup(clanTag)
    clanToTHLevels = printEnemiesTHDistribution(clanTag, cwlData)
    printRounds(clanTag, cwlData, clanToTHLevels)
    print()

