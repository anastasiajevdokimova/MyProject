from tkinter import *
from random import *
from myfunctions import *

EST='qwertyuiopüõasdfghjklöäzxcvbnm'
estv=loe_fail("Estv.txt")
rusv=loe_fail("Rusv.txt")
estlm=loe_fail("Estlm.txt")
ruslm=loe_fail("Ruslm.txt")

win=Tk()
win.title("Let's learn Estonian verbs")
win.geometry('1000x1000')
btnM=Button(win, text="Настоящее время \nOlevik",width=15,height=3)
btnM1=Button(win, text="Прошедшее время \nLihtminevik",width=15,height=3)

btnM.pack(anchor=NW)
btnM1.pack(anchor=N)

root.maintloop()