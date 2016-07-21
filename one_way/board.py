from block import T,O,I,L,J,S,Z
from copy import deepcopy
from msvcrt import getwch, kbhit
from time import time, sleep
from random import choice


class Board:
    """ tetris inner board , recording the state of blocks. 0 means empty"""
    block_table = (T,O,I,L,J,S,Z)

    def __init__(self, row_size, col_size):
        self.row_size = row_size
        self.col_size = col_size
        self.board = []
        self.block = None
        self.score = 0

        for i in range(row_size):
            li = [0] * col_size
            self.board.append(li)

        self.newBlock()

    def draw(self):
        
        # merge play_block into a tmp  board
        tmp_board = deepcopy(self.board) 
        all_pos = self.block.tellAllPos()
        for row, col in all_pos:
            tmp_board[row][col] = 1
    
        #clear screen
        print('\n' * 25)

        # print all board
        print(' '*7,'我的俄羅斯方塊  分數：',self.score)
        print(' '*7, end='')
        for i in range(self.col_size) :
            print( format(i,'2') , end='')
        print()

        for j, row in  enumerate(tmp_board):
            print(' '*4, format(j,'2') , end='')
            for col in row :
                if col >= 1:
                    print('\u25A0', end='')
                    #print('國', end='')
                else:
                    print('\u25A1', end='')
                    #print('回', end='')
            print()

        print(' '*7, end='')
        #print('積木位置:', all_pos )

    def newBlock(self):
        obj = choice(self.block_table)
        t = obj.block_type
        self.block = obj(0, self.col_size//2 - 1)

    def mergeBlock(self):
        for row, col in self.block.tellAllPos():
            self.board[row][col] = self.block.color_num
        self.eraseBlock()
        self.newBlock()

    def eraseBlock(self):
        #collect block row number
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

    def moveBottom(self):
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
                break
    def turnClockwise(self):
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




    

