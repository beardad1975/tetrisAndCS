from tkinter import *
from random import choice

boardGui = [] 

def change_color():
    for i in range(20):
        for j in range(10):
            s = choice(['black','black','black','black','black','black','green','yellow','red'])
            boardGui[i][j].config(bg=s)

    root.after(1000, change_color)

 

root = Tk()


for i in range( 20):
    tmp_list = []
    for j in range(10): 
        textObj =  Label(root,width=2 ,relief=RAISED,bg="black", text="")
        textObj.grid(row=i,column=j)
        tmp_list.append(textObj)
    boardGui.append(tmp_list)

root.after(1000, change_color )

root.mainloop()