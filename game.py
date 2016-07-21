from block import Block
from copy import deepcopy
from msvcrt import getwch, kbhit
from time import time, sleep
from random import choice
import sys

class Game:
    
    

    def __init__(self, row_size, col_size):
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

        for i in range(row_size):
            li = [0] * col_size
            self.board.append(li)

        self.newBlock()

    def draw(self):
        #繪圖
        
        # 把方塊和棋盤合到暫時棋盤
        tmp_board = deepcopy(self.board) 
        all_pos = self.block.tellAllPos()
        for row, col in all_pos:
            tmp_board[row][col] = self.block.color_num
    
        #清除螢幕
        print('\n' * 25)

        #印出暫時棋盤
        print(' '*7,'我的俄羅斯方塊  分數：',self.score)
        print(' '*7, end='')
        for i in range(self.col_size) :
            print( format(i,'2') , end='')
        print()

        for j, row in  enumerate(tmp_board):
            print(' '*4, format(j,'2') , end='')
            for col in row :
                if col >= 1:
                    print('■', end='')
                    
                else:
                    print('□', end='')
                    
                    
            print()

        print(' '*7, end='')
        

        
        
    def newBlock(self):
        #新方塊
        self.block = Block(0, self.col_size//2)

        for row, col in self.block.tellAllPos():
            if self.board[row][col] > 0:
                self.mergeBlock()
                self.draw()
                print("遊戲結束")
                sys.exit()
        
    def mergeBlock(self):
        #合併方塊
        for row, col in self.block.tellAllPos():
            self.board[row][col] = self.block.color_num
        #self.eraseBlock()
        #self.newBlock()

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
            sleep(0.4)
            need_erased_row.sort()
            need_erased_row.reverse()
            for n in need_erased_row:
                self.board.pop(n)
                
            for _ in range(row_num):
                self.board.insert(0, [0]*self.col_size)

            self.score += row_num

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
        #下移方塊
        
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
        while True:
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




    

