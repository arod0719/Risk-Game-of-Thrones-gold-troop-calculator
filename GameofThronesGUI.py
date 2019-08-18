from tkinter import *
import os

directory_path = os.path.dirname(__file__) #used to find logos for each unit type


root = Tk()
root.title("Game of Thrones Risk - Calculator") #name of the gui
root.geometry("470x350") #gui size

#Each image  is processed and added to the gui 
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

gameofthrones = Label(text="Game of Thrones Risk - Calculator", font='Helvetica 18 bold') #title
gameofthrones.grid(row=0, column=1, columnspan=2)
#used to have words matching the logo for usability
Label(text="Castles",relief=RIDGE, width=15).grid(row=1,column=1)
Label(text="Lands",relief=RIDGE, width=15).grid(row=2,column=1)
Label(text="Ports",relief=RIDGE, width=15).grid(row=3,column=1)
Label(text="Bonus Points",relief=RIDGE, width=15).grid(row=4,column=1)
Label(text="Troops",relief=RIDGE, width=15).grid(row=5,column=1, pady=(50,0))
Label(text="Gold",relief=RIDGE, width=15).grid(row=6,column=1)

#creates answer fields to allow user to type in values
entryCastle = Entry(root,justify='center')
entryCastle.grid(row=1,column=2)
entryLand = Entry(root,justify='center')
entryLand.grid(row=2,column=2)
entryPort = Entry(root,justify='center')
entryPort.grid(row=3,column=2)
entryBonus = Entry(root,justify='center')
entryBonus.grid(row=4,column=2)
entryAnswerTroops = Entry(root, state="readonly",justify='center')
entryAnswerTroops.grid(row=5, column=2, pady=(50,0))
entryAnswerGold = Entry(root, state="readonly",justify='center')
entryAnswerGold.grid(row=6, column=2)

def calculate():
    try:
        #begins calculating results
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
        #if something goes wrong, show "error"
        entryAnswerTroops.configure(state='normal')
        entryAnswerTroops.delete(0,END)
        entryAnswerTroops.insert(0, "Error")
        entryAnswerTroops.configure(state='readonly')
        entryAnswerGold.configure(state='normal')
        entryAnswerGold.delete(0,END)
        entryAnswerGold.insert(0, "Error")
        entryAnswerGold.configure(state='readonly')

def reset(): 
    #clears all entries
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
    
    

calculation = Button(root, text="Calculate", command=calculate) #button to call the calculate function
calculation.grid(row=5, column=0, pady=(50,0))

reset = Button(root, text="Clear", command=reset) #button to call the reset function
reset.grid(row=6, column=0)



root.mainloop()
