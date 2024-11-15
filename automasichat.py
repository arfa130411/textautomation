import pyautogui as pg
import time

limit = input("Masukkan limit teks:")
message = input("Enter message:")
i = 0
time.sleep(5)

while i < int(limit):
    pg.typewrite(message)

    pg.press("Enter")

    i+=1
