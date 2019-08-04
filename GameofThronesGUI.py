from tkinter import *
import os

directory_path = os.path.dirname(__file__)


root = Tk()
root.title("Game of Thrones Risk - Calculator")
root.geometry("470x350")

image1 = PhotoImage(file = os.path.join(directory_path, 'castle.gif'))
label = Label(image = image1)
label.grid(row=1,column=0)

image2 = PhotoImage(file = os.path.join(directory_path, 'land.gif'))
label = Label(image = image2)
label.grid(row=2,column=0)

image3 = PhotoImage(file = os.path.join(directory_path, 'port.gif'))
label = Label(image = image3)
label.grid(row=3,column=0)

image4 = PhotoImage(file = os.path.join(directory_path, 'bonus.gif'))
label = Label(image = image4)
label.grid(row=4,column=0)

gameofthrones = Label(text="Game of Thrones Risk - Calculator", font='Helvetica 18 bold')
gameofthrones.grid(row=0, column=1, columnspan=2)
Label(text="Castles",relief=RIDGE, width=15).grid(row=1,column=1)
Label(text="Lands",relief=RIDGE, width=15).grid(row=2,column=1)
Label(text="Ports",relief=RIDGE, width=15).grid(row=3,column=1)
Label(text="Bonus Points",relief=RIDGE, width=15).grid(row=4,column=1)
Label(text="Troops",relief=RIDGE, width=15).grid(row=5,column=1, pady=(50,0))
Label(text="Gold",relief=RIDGE, width=15).grid(row=6,column=1)

entryCastle = Entry(root)
entryCastle.grid(row=1,column=2)
entryLand = Entry(root)
entryLand.grid(row=2,column=2)
entryPort = Entry(root)
entryPort.grid(row=3,column=2)
entryBonus = Entry(root)
entryBonus.grid(row=4,column=2)
entryAnswerTroops = Entry(root, state="readonly")
entryAnswerTroops.grid(row=5, column=2, pady=(50,0))
entryAnswerGold = Entry(root, state="readonly")
entryAnswerGold.grid(row=6, column=2)

def calculate():
    try:
        entryAnswerTroops.configure(state='normal')
        entryAnswerTroops.delete(0,END)
        entryAnswerTroops.configure(state='readonly')
        entryAnswerGold.configure(state='normal')
        entryAnswerGold.delete(0,END)
        entryAnswerGold.configure(state='readonly')
        castle = (int(entryCastle.get()))
        land = (int(entryLand.get()))
        port = (int(entryPort.get()))
        bonus = (int(entryBonus.get()))
        troops = (castle+land)//3 + bonus
        gold = (troops + port) * 100
        entryAnswerTroops.configure(state='normal')
        entryAnswerTroops.delete(0,END)
        entryAnswerTroops.insert(0, troops)
        entryAnswerTroops.configure(state='readonly')
        entryAnswerGold.configure(state='normal')
        entryAnswerGold.delete(0,END)
        entryAnswerGold.insert(0, gold)
        entryAnswerGold.configure(state='readonly')
        
    except:
        entryAnswerTroops.configure(state='normal')
        entryAnswerTroops.delete(0,END)
        entryAnswerTroops.insert(0, "Error")
        entryAnswerTroops.configure(state='readonly')
        entryAnswerGold.configure(state='normal')
        entryAnswerGold.delete(0,END)
        entryAnswerGold.insert(0, "Error")
        entryAnswerGold.configure(state='readonly')

def reset():
    entryCastle.delete(0,END)
    entryLand.delete(0,END)
    entryPort.delete(0,END)
    entryBonus.delete(0,END)
    entryAnswerTroops.configure(state='normal')
    entryAnswerTroops.delete(0,END)
    entryAnswerTroops.configure(state='readonly')
    entryAnswerGold.configure(state='normal')
    entryAnswerGold.delete(0,END)
    entryAnswerGold.configure(state='readonly')
    
    

calculation = Button(root, text="Calculate", command=calculate)
calculation.grid(row=5, column=0, pady=(50,0))

reset = Button(root, text="Clear", command=reset)
reset.grid(row=6, column=0)



root.mainloop()
