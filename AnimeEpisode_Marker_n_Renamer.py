#######################################################################################################################

LastEp = 892
loc = "//NAS/.Anime$/One Piece/Episodes/9.Yonko Saga"
showname = "One Piece"
url = "https://www.animefillerlist.com/shows/one-piece"

#######################################################################################################################

import requests
import shutil
import os
import time
from bs4 import BeautifulSoup

animeinfo = []

# Defing Funtion to get info about the Series Episode and add it to 'animeinfo' array
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


# Funtion to ShowList 'animeinfo'
def showlist():
    print(animeinfo)


########################################################################################################################
# Running the Get_Info() funtion
get_info()
# showlist()

# Just Print Showname for identifier
print(showname)

# Serching every episode in the location
files = os.listdir(loc)
for name in files:
    if ".mkv" in name:
        ep = ""
        flag = 0
        for i in range(len(name)):

            # Storing Episode number in ep variable ,3 if statment as number can of of * ,** ,*** order
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
                EpType = animeinfo[EPint - 1][1]  # Assigning Episode type to Eptype variable ie filler or not

            # Just changing the wring format of Eptype ie from 'Filler' to '[Filler]'
            print(EPint, " - ", EpType)
            if EpType == "Filler":
                EpType = " [Filler]"
            elif EpType == "Mostly Filler":
                EpType = " [Mostly Filler]"
            else:
                EpType = ""
        # Setting up path of the file to start the rename process
        if flag == 1 and EPint > LastEp:
            oldname = loc + "/" + name
            newname = loc + "/" + showname + " - " + ep + " [720p]" + EpType + ".mkv"

            # print(oldname)
            try:
                shutil.move(oldname, newname)
            except EnvironmentError:
                print(ep + " - ERROR")
            else:
                print(ep + " - Renamed")
print("Closing in 5 Sec")
time.sleep(5)
