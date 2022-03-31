#   Use it to know the tahajjud prayer time

"""
----------------------------------------------------------------------------------------------
The best time to perform the tahajjud prayer is at the last third of the night. So this python
script is going to calculate exactly the beginning of the last third of a night and the end.
-----------------------------------------------------------------------------------------------
"""
#   --------------- How is work
"""
----------------------------------------------------------------------------------------------
To begin, all you have to do is enter the Maghrib prayer period and the Fajr prayer period.
-----------------------------------------------------------------------------------------------
"""


import os
brand = '''
 _____     _            _  _           _      _   _                               _            _       _             
|_   _|_ _| |__   __ _ (_)(_)_   _  __| |    | |_(_)_ __ ___   ___       ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
  | |/ _` | '_ \ / _` || || | | | |/ _` |    | __| | '_ ` _ \ / _ \     / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
  | | (_| | | | | (_| || || | |_| | (_| |    | |_| | | | | | |  __/    | (_| (_| | | (__| |_| | | (_| | || (_) | |   
  |_|\__,_|_| |_|\__,_|/ |/ |\__,_|\__,_|     \__|_|_| |_| |_|\___|     \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                     |__/__/                                                                                   
'''

logo = '''
 __  __           _           _                _                _    _           _          _     
|  \/  | __ _  __| | ___     | |__  _   _     | |__   ___ _ __ | | _| |__   __ _(_)_ __ ___| |__  
| |\/| |/ _` |/ _` |/ _ \    | '_ \| | | |    | '_ \ / _ \ '_ \| |/ / '_ \ / _` | | '__/ _ \ '_ \ 
| |  | | (_| | (_| |  __/    | |_) | |_| |    | |_) |  __/ | | |   <| | | | (_| | | | |  __/ | | |
|_|  |_|\__,_|\__,_|\___|    |_.__/ \__, |    |_.__/ \___|_| |_|_|\_\_| |_|\__,_|_|_|  \___|_| |_|
                                    |___/                                          
'''

"""
----------------------------------------------------------------------------------------------
This function is used for to print into the console
-----------------------------------------------------------------------------------------------
"""

def writeTxt(txt):
    print("------------------------------------------------------------------")
    print(txt)
    print("------------------------------------------------------------------")

"""
----------------------------------------------------------------------------------------------
This function is used to get the Maghrib prayer time and the Fajr prayer time 
-----------------------------------------------------------------------------------------------
"""

def settings(txt, lang):
    if txt == 'maghribHour':
        if lang == 'fr':
            writeTxt("Saisir l'heure du coucher du soleil [ format 24h ] [ Heures ]")
        else:
            writeTxt("Enter the hour time of the sunset [ 24h format ] [ Hours ]")
        settings.maghribHour = input(">  ")
    elif txt == 'fajrHour':
        if lang == 'fr':
            writeTxt("Saisir l'heure de la prière du Fajr [ format 24h ] [ Heures ]")
        else:
            writeTxt("Enter the time of the Fajr prayer [ 24h format ] [ Hours ]")
        settings.fajrHour = input(">  ")
    elif txt == 'maghribMinutes':
        if lang == 'fr':
            writeTxt("Saisir les minutes du coucher du soleil [ Minutes ]")
        else:
            writeTxt("Enter the munites of the sunset [ Minutes ]")
        settings.maghribMinutes = input(">  ")
    elif txt == 'fajrMinutes':
        if lang == 'fr':
            writeTxt("Saisir les minutes de la prière du Fajr [ Minutes ]")
        else:
            writeTxt("Enter the minutes of the Fajr prayer [ Minutes ]")
        settings.fajrMinutes = input(">  ")
    else:
        writeTxt("Undefined")

"""
----------------------------------------------------------------------------------------------
This function is used to calculate the begining of the last third of the night and the end 
-----------------------------------------------------------------------------------------------
"""

def calculator(lang): 
    maghribFajrHour = int(settings.maghribHour) - int(settings.fajrHour)
    lastThirdMinutes = int(maghribFajrHour) / 3
    maghribFajrMinutes = int(settings.maghribMinutes) - int(settings.fajrMinutes)
    
    if int(settings.fajrHour) <= 9:
        settings.fajrHour = settings.fajrHour.zfill(2)
    if int(settings.fajrMinutes) <= 9:
        settings.fajrMinutes = str(int(settings.fajrMinutes) - 1).zfill(2)

    beforeFajr = "{0}:{1}".format(
        settings.fajrHour, settings.fajrMinutes)

    lastThird = '{0:02.0f}:{1:02.0f}'.format(
        *divmod(lastThirdMinutes * 60, 60 + maghribFajrMinutes))

    if lang == 'en': 
        writeTxt("The last third of the night to pray the tahajjud prayer starts at {0} and end at {1}".format(lastThird, beforeFajr))
    else:
        writeTxt("Le dernier tiers de la nuit pour prier la prière de tahajjud commence à {0} et se terminent à {1}".format(lastThird, beforeFajr))

#   --------------- Clearning the console and running the code

os.system('clear')
print(brand)
print(logo)

#   --------------- Setting the desired language

writeTxt("Saisir 'fr': Pour Français | Enter 'en': For English")
lang =  input(">  ")

#   --------------- Getting Maghrib prayer time

settings('maghribHour', lang)
settings('maghribMinutes', lang)

#   --------------- Getting Fajr prayer time

settings('fajrHour', lang)
settings('fajrMinutes', lang)

#   --------------- Outputing the begining and the end of the last third of the night

calculator(lang)
