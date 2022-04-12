import pyautogui,time,os,datetime

time.sleep(2)
print("start")
while True:
    #if datetime.datetime.now().hour == 4:
      # os.system ('shutdown /s /t 10')
      # break




    position = pyautogui.locateOnScreen(r'img\confermmeta.JPG', confidence=0.8)
    if position != None:
        pyautogui.moveTo(position[0] + 25, position[1] + 25)
        pyautogui.click()
    position = pyautogui.locateOnScreen(r'img\start.JPG', confidence=0.8)
    if position != None:
         pyautogui.moveTo(position[0] + 25, position[1] + 25)
         pyautogui.click()
    position = pyautogui.locateOnScreen(r'img\findanoder.JPG', confidence=0.8)
    if position != None:
         pyautogui.moveTo(position[0] + 25, position[1] + 25)
         pyautogui.click()
    position = pyautogui.locateOnScreen(r'img\1st.JPG', confidence=0.9)
    if position != None:
        pyautogui.click()
        pyautogui.scroll(-50)
    time.sleep(1)
    position = pyautogui.locateOnScreen(r'img\nextmatch.JPG', confidence=0.5)
    if position != None:
        pyautogui.moveTo(position[0] + 25, position[1] + 25)
        pyautogui.click()

    position = pyautogui.locateOnScreen(r'img\inderst.JPG', confidence=0.8)
    if position != None:
        pyautogui.moveTo(position[0] + 10, position[1] + 20)
        pyautogui.click()
        time.sleep(1)
        position = pyautogui.locateOnScreen(r'img\url.JPG', confidence=0.8)
        if position != None:
            pyautogui.moveTo(position[0] + 15, position[1] + 20)
            pyautogui.click()
            pyautogui.press('enter')
            time.sleep(7)