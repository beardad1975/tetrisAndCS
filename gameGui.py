from block import T_Shape,O_Shape,I_Shape,L_Shape,J_Shape,S_Shape,Z_Shape
from copy import deepcopy
from msvcrt import getwch, kbhit
from time import time, sleep
from random import choice, randrange
from tkinter.messagebox import showinfo
from tkinter import *


class GameGui(Frame):
    

    def __init__(self, row_size, col_size, parent,title='我的俄羅斯方塊'):
        #設置
        #橫列數
        self.row_size = row_size
        #直行數
        self.col_size = col_size
        #棋盤
        self.board = []
        #方塊
        self.block = None
        #得分
        self.score = 0
        #標題
        self.title = title

        for i in range(row_size):
            li = [0] * col_size
            self.board.append(li)

        self.newBlock()
        
        Frame.__init__(self, parent)
        
        Label(self,text=self.title).pack(side=TOP)
        self.score_label = Label(self, text='分數： 0')
        self.score_label.pack(side=TOP)

        self.board_frame = Frame(self)
        self.board_frame.pack(side=TOP)
        
        self.gui_board = []
        for i in range(row_size):
            li = []
            for j in range(col_size):
                ent = Label(self.board_frame, text='',width=2,relief=GROOVE,bg='black')
                ent.grid(row=i, column=j, sticky=NSEW)
                li.append(ent)
            self.gui_board.append(li)
            
        

    def update_score(self):
        #更新分數
        
        self.score_label.config(text='分數： {}'.format(self.score))        



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
                if col >= 1:
                    label = self.gui_board[row_index][col_index]
                    label.config(bg='yellow',relief=RAISED)
                else:
                    label = self.gui_board[row_index][col_index]
                    label.config(bg='black',relief=GROOVE)
        self.update()
            
            
       

    def newBlock(self):
        #新方塊
        block_list = (T_Shape,O_Shape,I_Shape,L_Shape,J_Shape,S_Shape,Z_Shape)
        obj = choice(block_list)
        
        self.block = obj(0, self.col_size//2 - 1)
        


        for row, col in self.block.tellAllPos():
            if self.board[row][col] > 0:
                #遊戲結束
                self.board_frame.after_cancel(self.after_id)
                showinfo('不', '遊戲結束')
                Frame.quit(self)
                break

    def mergeBlock(self):
        #合併方塊
        for row, col in self.block.tellAllPos():
            self.board[row][col] = self.block.color_num
        
        


    def eraseBlock(self):
    
        #消方塊
        row_set = set()
        for r, _ in self.block.tellAllPos():
            row_set.add(r)

        need_erased_row = []
        for rs in row_set:
            count = 0
            for i in self.board[rs]:
                if i : count+=1
            if count == self.col_size: need_erased_row.append(rs)

        row_num = len(need_erased_row)
        if row_num:
            self.draw()
            #sleep(0.3)            
            need_erased_row.sort()
            need_erased_row.reverse()
            for n in need_erased_row:
                self.board.pop(n)
                #self.board.insert(0, [0]*self.col_size)
                #self.draw()
                #sleep(0.1)
            for _ in range(row_num):
                self.board.insert(0, [0]*self.col_size)

            self.score += row_num
            self.update_score()
        
        

    def moveRight(self):
        #右移方塊
        move_flag = True
        for row, col in self.block.tellRightPos():
            if col >= self.col_size :
                move_flag = False
                break
            elif self.board[row][col] :
                move_flag = False
                break
        if move_flag:
            self.block.moveRight()

            
    def moveLeft(self):
        #左移方塊
        move_flag = True
        for row, col in self.block.tellLeftPos():
            if col < 0 :
                move_flag = False
                break
            elif self.board[row][col] :
                move_flag = False
                break
        if move_flag:
            self.block.moveLeft()

    def moveDown(self):
        # 下移方塊
        move_flag = True
        for row, col in self.block.tellDownPos():
            if row >= self.row_size:
                move_flag = False
                break
            elif self.board[row][col] :
                move_flag = False
                break
        if move_flag:
            self.block.moveDown()
        else: #merge
            self.mergeBlock()
            self.eraseBlock()
            self.newBlock()

    def moveBottom(self):
        #直落方塊
        while self.block:
            # move or merge
            move_flag = True
            for row, col in self.block.tellDownPos():
                if row >= self.row_size:
                    move_flag = False
                    break
                elif self.board[row][col] :
                    move_flag = False
                    break
            if move_flag:
                self.draw()
                self.block.moveDown()
            else: #merge
                
                self.mergeBlock()
                self.eraseBlock()
                self.newBlock()
                break
                
    def turnClockwise(self):
        #順時針旋轉方塊
        if self.block.block_type == 'O':
            return

        turn_flag = True
        for row, col in self.block.tellClockwisePos():
            if col < 0 or col >= self.col_size  \
                or row < 0 or row >= self.row_size:
                turn_flag = False
                break
            elif self.board[row][col] :
                turn_flag = False
                break
        if turn_flag:
            self.block.turnClockwise()

    def turnCounter(self):
        #逆時針旋轉方塊
        if self.block.block_type == 'O':
            return

        turn_flag = True
        for row, col in self.block.tellCounterPos():
            if col < 0 or col >= self.col_size  \
                or row < 0 or row >= self.row_size:
                turn_flag = False
                break
            elif self.board[row][col] :
                turn_flag = False
                break
        if turn_flag:
            self.block.turnCounter()




    

