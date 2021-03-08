#   Use it to know the Tahajjud time

"""
----------------------------------------------------------------------------------------------
The Tahajjud prayer is performed in the last third of the night after awakening from sleep. 
So this python script will calculate exactly the start of the last third of a night and the end.
-----------------------------------------------------------------------------------------------
"""
#   --------------- How is work
"""
----------------------------------------------------------------------------------------------
To get the start of the last third and the end of the night you just need to input the Maghrib prayer time and the Fajr prayer time.
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


def writeTxt(txt):
    print("------------------------------------------------------------------")
    print(txt)
    print("------------------------------------------------------------------")


def settings(txt, lang):
    if txt == 'maghribHour':
        if lang == 'fr':
            writeTxt("Réglez l'heure Maghrib [Heure] au format 24h")
        else:
            writeTxt("Set the Maghrib time [Hour] in 24h format")
        settings.maghribHour = input(">  ")
    elif txt == 'fajrHour':
        if lang == 'fr':
            writeTxt("Réglez l'heure Fajr [Heure] au format 24h")
        else:
            writeTxt("Set the Fajr time [Hour] in 24h format")
        settings.fajrHour = input(">  ")
    elif txt == 'maghribMinutes':
        if lang == 'fr':
            writeTxt("Réglez l'heure Maghrib [Minutes]")
        else:
            writeTxt("Set the Maghrib time [Minutes]")
        settings.maghribMinutes = input(">  ")
    elif txt == 'fajrMinutes':
        if lang == 'fr':
            writeTxt("Réglez l'heure Fajr [Minutes]")
        else:
            writeTxt("Set the Fajr time [ Minutes ]")
        settings.fajrMinutes = input(">  ")
    else:
        writeTxt("Undefined")


os.system('clear')
print(brand)
print(logo)

settings('maghribHour', '')

settings('maghribMinutes', '')

settings('fajrHour', '')

settings('fajrMinutes', '')

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


writeTxt("Time to pray Tahajjud start at {0} and end at {1}".format(
    lastThird, beforeFajr))
