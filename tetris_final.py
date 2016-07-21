
from msvcrt import getwch, kbhit
from time import time, sleep
from random import choice
from game import Game
from block import T_Shape, O_Shape
import sys

class MyGame(Game):
    def newBlock(self):
        #新方塊
        block_list = [T_Shape, O_Shape]
        obj = choice(block_list)
        self.block = obj(0, self.col_size//2)

        for row, col in self.block.tellAllPos():
            if self.board[row][col] > 0:
                self.mergeBlock()
                self.draw()
                print("遊戲結束")
                sys.exit()


if __name__ == "__main__":
    tetris = MyGame(20, 10)
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


        elapsed = time() - previous_time
        if elapsed > 2:
            previous_time = time()
            tetris.moveDown()
            tetris.draw()

    

