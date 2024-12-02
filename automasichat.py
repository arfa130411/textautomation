import pyautogui as pg
import time

print('2024 Arfa Abdallah Wahab')
limit = input("Masukkan limit teks : ")
message = input("Masukkan pesan/teks : ")
i = 0
time.sleep(5)

while i < int(limit):
    pg.typewrite(message)

    pg.press("Enter")

    i+=1
