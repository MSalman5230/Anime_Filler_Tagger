
########################################################################################################################

LastEp=891
#loc = "//NAS/.Anime$/One Piece/Episodes/9.Yonko Saga"
loc = r"\\SERVO\anime\One Piece\Episodes\OP NEW"
showname = 'One Piece'
url= 'https://www.animefillerlist.com/shows/one-piece'
default_quality=" [720p]"
#######################################################################################################################

import requests
import shutil
import os
import time
from bs4 import BeautifulSoup

animeinfo = []
def get_info():

    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, "lxml")

    for epinfo in soup.find_all("tr", {"class": ["canon odd", "canon even", "filler odd", "filler even"]}):
        # print(epinfo)
        epno = epinfo.find("td", {"class": "Number"}).text
        type = epinfo.find("td", {"class": "Type"}).text
        # print(epno + " : " + type)
        global animeinfo
        animeinfo.append([epno, type])


def showlist():
    print(animeinfo)

def get_quality(name):
    print("CHECKING",'720p' in name)
    if '480p' in name:
        return " [480p]"
    elif '720p' in name:
        return " [720p]"
    elif '1080p' in name:
        return " [1080p]"
    else:
        return default_quality

########################################################################################################################
print("Started")
get_info()
# showlist()

print(showname)
files = os.listdir(loc)
for name in files:
    if ".mkv" in name:
        ep = ""
        flag = 0
        for i in range(len(name)):
            
            if (name[i].isdigit() and name[i + 1].isdigit() and name[i + 2].isdigit() and name[i + 3].isdigit()) and (name[i + 4] == " " or name[i + 4] == "_" or name[i + 4] == "."):  # For Format ***
                # print(name)
                ep = name[i]
                ep = ep + name[i + 1]
                ep = ep + name[i + 2]
                ep = ep + name[i + 3]
                flag = 1
                break


            if (name[i].isdigit() and name[i + 1].isdigit() and name[i + 2].isdigit()) and (name[i + 3] == " " or name[i + 3] == "_" or name[i + 3] == "."):  # For Format ***
                # print(name)
                ep = name[i]
                ep = ep + name[i + 1]
                ep = ep + name[i + 2]
                flag = 1
                break

            elif (name[i].isdigit() and name[i + 1].isdigit()) and (name[i + 2] == " " or name[i + 2] == "_" or name[i + 2] == "."):  # For Format **
                ep = "0"
                ep = ep + name[i]
                ep = ep + name[i + 1]
                flag = 1
                break

            elif (name[i].isdigit()) and (name[i + 1] == " " or name[i + 1] == "_" or name[i + 1] == "."):  # For Format *
                ep = "00"
                ep = ep + name[i]
                flag = 1
                break

        # print(ep)
        EPint = ep
        if EPint.isdigit() and flag == 1:
            EPint = int(EPint)
            EpType = ""
            if EPint <= len(animeinfo):
                # print(EPint)
                EpType = animeinfo[EPint - 1][1]

            print(EPint, " - ", EpType)
            if EpType == "Filler":
                EpType = " [Filler]"
            elif EpType == "Mostly Filler":
                EpType = " [Mostly Filler]"
            else:
                EpType = ""

        if flag == 1 and EPint > LastEp:
            print(name)
            quality=get_quality(name)
            oldname = loc + "/" + name
            newname = loc + "/" + showname + " - " + ep + quality + EpType + ".mkv"

            # print(oldname)
            try:
                shutil.move(oldname, newname)
            except EnvironmentError:
                print(ep + " - ERROR")
            else:
                print(ep + " - Renamed")
print("Closing in 10 Sec")
time.sleep(10)