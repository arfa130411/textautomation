import pyautogui as pg
from random import choice as c
import time

li = ['halo', 'hai', 'bang', 'kang', 'bro', 'mba', 'mas', 'sis', 'ngab']

i = 0

print("Program ini sangat bisa digunakan untuk anda yang memiliki teman yang slow respon, hehehehehehehehe")
gender = input("Masukkan jenis kelamin L/P: ")
z = input("Masukkan  limit pesan: ")

if gender == 'L':
        li.remove('mba')
        li.remove('sis')
        time.sleep(5)
        while i < int(z):
                pg.typewrite(c(li))
                pg.press("Enter")
        i+=1

if gender == 'P':
        li.remove('mas')
        li.remove('bang')
        li.remove('kang')
        li.remove('bro')
        li.remove('ngab')
        time.sleep(5)
        while i < int(z):
            pg.typewrite(c(li))
            pg.press("Enter")

        i+=1
    


