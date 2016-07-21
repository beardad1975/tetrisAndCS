
from msvcrt import getwch, kbhit
from time import time, sleep
from random import choice
from game import Game
from serial import Serial
from copy import deepcopy
from block import T_Shape, O_Shape, I_Shape
import sys


class LedGame(Game):

    def __init__(self):
        Game.__init__(self, 8,8)
        self.serial = Serial("com23", 38400)
        
        sleep(3)

    def newBlock(self):
        #新方塊
        block_list = [T_Shape, O_Shape, I_Shape]
        obj = choice(block_list)
        self.block = obj(0, self.col_size//2)

        for row, col in self.block.tellAllPos():
            if self.board[row][col] > 0:
                self.mergeBlock()
                self.draw()
                print("遊戲結束")
                sys.exit()
        
    def draw(self):
        #繪圖
        Game.draw(self)
        
        # 把方塊和棋盤合到暫時棋盤
        tmp_board = deepcopy(self.board) 
        all_pos = self.block.tellAllPos()
        for row, col in all_pos:
            tmp_board[row][col] = self.block.color_num
    
        #清除螢幕
        

        #印出暫時棋盤
        
        
       
        num_list = []
        for row_num, row in  enumerate(tmp_board):
            sum = 0
            row.reverse()
            for col_num, col in enumerate(row):
                if col > 0 :
                    sum = sum +  2 ** col_num
                
            num_list.append(sum)        
                    
        self.serial.write(bytes(num_list))    

                



if __name__ == "__main__":
    tetris = LedGame()
    tetris.draw()

    previous_time = time()

    key = ''
    while True:
        
        if kbhit():
            key = getwch()
            if key == '4':
                tetris.moveLeft()
            elif key == '6':
                tetris.moveRight()
            elif key == '5':
                tetris.moveDown()
            elif key == ' ':
                tetris.moveBottom()
            elif key == '8':
                tetris.turnClockwise()
            elif key == 'z':
                tetris.turnCounter()
            elif key == 'q':
                break

            tetris.draw()


        #elapsed = time() - previous_time
        #if elapsed > 2:
        #    previous_time = time()
        #    tetris.moveDown()
        #    tetris.draw()

    

