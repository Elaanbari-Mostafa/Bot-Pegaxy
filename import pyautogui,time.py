from datetime import date
import pyautogui,time,datetime,os
from datetime import datetime

sec = 30
print("debut hh")
while True:
    time.sleep(4)
    pyautogui.click()
    dateNow = datetime.now().hour
    if dateNow == 3:
        print("hh nady")
        os.system(f'shutdown /s /t {sec}')
        fichier_source = open(r"Nouveau document texte (3).txt" ,"w")
        fichier_source.write("nady hh algo yt time hour = " + dateNow)
        fichier_source.close()
        break
    time.sleep(4)