
from tkinter import *
from gameGui import GameGui
from copy import deepcopy

class MyGameGui(GameGui):


        

    def onLeftKey(self, event):
        self.moveLeft()
        self.draw()

    def onRightKey(self, event):
        self.moveRight()
        self.draw()        

    def onBottomKey(self, event):
        self.moveBottom()
        self.draw()        

    def onDownKey(self, event):
        self.moveDown()
        self.draw() 

    def onTurnKey(self, event):
        self.turnClockwise()
        self.draw()        

    def draw(self):
        #繪圖
        #把方塊和棋盤合到暫時棋盤
        tmp_board = deepcopy(self.board) 
        if self.block:
            all_pos = self.block.tellAllPos()
            for row, col in all_pos:
                tmp_board[row][col] = self.block.color_num
    
        #印到Gui的棋盤
        for row_index, row in enumerate(tmp_board):
            for col_index, col in enumerate(row) :
                if col == 1:
                    label = self.gui_board[row_index][col_index]
                    label.config(bg='yellow',relief=RAISED)
                elif col == 2:
                    label = self.gui_board[row_index][col_index]
                    label.config(bg='red',relief=RAISED)
                elif col == 3:
                    label = self.gui_board[row_index][col_index]
                    label.config(bg='pink',relief=RAISED)
                elif col == 4:
                    label = self.gui_board[row_index][col_index]
                    label.config(bg='green',relief=RAISED)
                elif col == 5:
                    label = self.gui_board[row_index][col_index]
                    label.config(bg='white',relief=RAISED)
                elif col == 6:
                    label = self.gui_board[row_index][col_index]
                    label.config(bg='blue',relief=RAISED)
                elif col == 7:
                    label = self.gui_board[row_index][col_index]
                    label.config(bg='orange',relief=RAISED)                    
                elif col == 0:
                    label = self.gui_board[row_index][col_index]
                    label.config(bg='black',relief=GROOVE)
        self.update()
    
    def period(self):
        self.moveDown()
        self.draw()
        
        self.id = self.after(2000, self.period)

root = Tk()

tetrisGui1p = MyGameGui(20, 10,root, title="1P")
tetrisGui1p.pack(side=LEFT)
tetrisGui1p.draw()

Label(root, text='').pack(side=LEFT)

tetrisGui2p = MyGameGui(20, 10,root,title="2P")
tetrisGui2p.pack(side=LEFT)
tetrisGui2p.draw()

root.bind("<a>", tetrisGui1p.onLeftKey)
root.bind("<d>", tetrisGui1p.onRightKey)
root.bind("<f>", tetrisGui1p.onBottomKey)
root.bind("<s>", tetrisGui1p.onDownKey)
root.bind("<w>", tetrisGui1p.onTurnKey)


root.bind("<Left>", tetrisGui2p.onLeftKey)
root.bind("<Right>", tetrisGui2p.onRightKey)
root.bind("<space>", tetrisGui2p.onBottomKey)
root.bind("<Down>", tetrisGui2p.onDownKey)
root.bind("<Up>", tetrisGui2p.onTurnKey)

tetrisGui1p.id = tetrisGui1p.after(2000, tetrisGui1p.period)
tetrisGui2p.id = tetrisGui2p.after(2000, tetrisGui2p.period)


root.focus()
root.mainloop()


    # def period(self):
        # if self.block:
            # self.moveDown()
            # self.draw()
        # self.after_id = self.board_frame.after(1000, self.period) 