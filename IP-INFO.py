#This is my first project...
import time
from gtts import gTTS
from playsound import playsound
from gtts.tts import Speed
import os
import urllib
import urllib.request
import json
import socket
import gi
from os import system, name
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


##colors
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'
BLACK   = '\033[40m'
RED0     = '\033[41m'
GREEN0   = '\033[42m'
YELLOW0  = '\033[43m'
BLUE0    = '\033[44m'
MAGENTA0 = '\033[45m'
CYAN0    = '\033[46m'
WHITE0   = '\033[47m'
RESET0   = '\033[49m'
BRIGHT    = '\033[1m'
DIM       = '\033[2m'
NORMAL    = '\033[22m'
RESET_ALL = '\033[0m'


print(RED +
'''
╭━━━━╮╱╱╱╱╭╮╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭━━━┳╮╱╱╱╱╱╱╱╱╱╭╮
┃╭╮╭╮┃╱╱╱╱┃┃╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃┃╱╱╱╱╱╱╱╱╭╯╰╮
╰╯┃┃┣┻━┳━━┫╰━┳━╮╭━━┫┃╭━━┳━━┳╮╱╭╮┃╰━╯┃┃╭━━┳━╮╭━┻╮╭╯
╱╱┃┃┃┃━┫╭━┫╭╮┃╭╮┫╭╮┃┃┃╭╮┃╭╮┃┃╱┃┃┃╭━━┫┃┃╭╮┃╭╮┫┃━┫┃
╱╱┃┃┃┃━┫╰━┫┃┃┃┃┃┃╰╯┃╰┫╰╯┃╰╯┃╰━╯┃┃┃╱╱┃╰┫╭╮┃┃┃┃┃━┫╰╮
╱╱╰╯╰━━┻━━┻╯╰┻╯╰┻━━┻━┻━━┻━╮┣━╮╭╯╰╯╱╱╰━┻╯╰┻╯╰┻━━┻━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┣━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━┻━━╯ credit: 5P1D3R9
''')
playsound('intro.mp3')
print(GREEN  + "            \033[47mYour Most Welcome Here\033[49m" + RESET0  )

time.sleep(2)

Nameofuser = input("~What's Your Name: " + YELLOW )

time.sleep(1)

print(RESET,GREEN+"~Your Most Welcome Dear:"+RESET,YELLOW,Nameofuser)

##for_speech
language = 'en'
SPEAK = "Your most welcome Dear" + Nameofuser
myobj = gTTS(text=SPEAK,lang=language,slow=False)

myobj.save("welcome.mp3")
playsound("welcome.mp3")
clear()

print(GREEN + '''
::: :::====                             
 ::: :::  ===                            
 === =======      JUST FOR EDU. PROPOSE                  
 === ===                  :joy:               
 === ===                                 
                                         
           ::: :::= === :::===== :::==== 
           ::: :::===== :::      :::  ===
           === ======== ======   ===  ===  
           === === ==== ===      ===  ===       
           === ===  === ===       ======  
''' + RESET)

while True:
    ip= input(CYAN + "Enter Your Target IP:"+ RESET)
    url = "http://ip-api.com/json/"
    nurl = url.replace(" ", "")
    response = urllib.request.urlopen(nurl+ip)
    data = response.read()
    values = json.loads(data)

    print(RED + "IP: "+RESET , GREEN + values['query'], RESET)
    print(RED + "STATUS: "+RESET , GREEN + values["status"], RESET)
    print(RED + "COUNTRY:"+ RESET , GREEN + values["country"], RESET)
    print(RED + "COUNTRY-CODE: "+RESET , GREEN + values["countryCode"], RESET)
    print(RED + "REGION: "+RESET , GREEN + values["region"], RESET)
    print(RED + "REGION-NAME: "+RESET , GREEN + values["regionName"], RESET)
    print(RED + "CITY: "+RESET , GREEN + values["city"], RESET)
    print(RED + "ZIP: "+RESET , GREEN + values["zip"], RESET)
    print(RED + "ISP: "+RESET , GREEN + values["isp"], RESET)

    print(MAGENTA , YELLOW0+ 'Information Extracted Just For You', Nameofuser + RESET,  RESET0)
    print(RED+ '''
     ________                __      __  __  
    /_  __/ /_  ____ _____  / /__    \ \/ /___  __  __/ /
     / / / __ \/ __ `/ __ \/ //_/     \  / __ \/ / / / / 
    / / / / / / /_/ / / / / ,<        / / /_/ / /_/ /_/  
   /_/ /_/ /_/\__,_/_/ /_/_/|_|      /_/\____/\__,_(_)   
        '''+RESET)
    exit()

    
       
