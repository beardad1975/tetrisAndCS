from copy import deepcopy
from msvcrt import getwch
from time import sleep

橫排數 =  8
直排數 = 4

class Game:
    棋盤 = []
    方塊位置 = None
    分數 = 0


def 設定():
    for _ in range(橫排數):
        row = [0] * 直排數
        Game.棋盤.append(row)

    新方塊()


def 新方塊():
    Game.方塊位置 = [0, 直排數//2 - 1]


def 繪圖():
    暫時棋盤 = deepcopy(Game.棋盤) 
    row, col = Game.方塊位置
    暫時棋盤[row][col] = 1

    #清除螢幕
    print('\n' * 25)

    print(' '*7, '迷你俄羅斯  分數：', Game.分數)
    print(' '*7, end='')
    for i in range(直排數) :
        print( format(i,'2') , end='')
    print()

    for num, row in  enumerate(暫時棋盤):
        print(' '*4, format(num,'2') , end='')
        for 格子 in row :
            if 格子 == 1 :
                print('\u25A0', end='')
                
            else:
                print('\u25A1', end='')
                
        print()

    print(' '*7, end='')
    print('方塊目前位置:', Game.方塊位置 )

    
def 合併方塊():
    row, col = Game.方塊位置
    Game.棋盤[row][col] = 1
    

def 消方塊():
    row = Game.方塊位置[0]

    計數 = 0
    for 格子 in Game.棋盤[row]:  
        if 格子: 
            計數 = 計數 + 1
    if 計數 == 直排數:
        
        繪圖()
        sleep(0.5)
        Game.棋盤.pop(row)
        Game.棋盤.insert(0, [0] * 直排數)
        Game.分數 = Game.分數 + 1

    新方塊()


def 右移方塊():
    row, col = Game.方塊位置
    下個位置 = [row, col+1]
    next_row, next_col = 下個位置

    if next_col > 直排數 - 1 :
        pass
    elif Game.棋盤[next_row][next_col] == 1:
        pass
    else:
        Game.方塊位置 = 下個位置

            
def 左移方塊():
    row, col = Game.方塊位置
    下個位置 = [row, col-1]
    next_row, next_col = 下個位置

    if next_col < 0  :
        pass
    elif Game.棋盤[next_row][next_col]:
        pass
    else: 
        Game.方塊位置 = 下個位置


def 下移方塊():
    row, col = Game.方塊位置
    下個位置 = [row+1, col]
    next_row, next_col = 下個位置

    if next_row >= 橫排數:
        合併方塊()
        消方塊()
    elif Game.棋盤[next_row][next_col] == 1:
        合併方塊()
        消方塊()
    else:
        Game.方塊位置 = 下個位置


def 直接落下方塊():
    while True:
        row, col = Game.方塊位置
        下個位置 = [row+1, col]
        next_row, next_col = 下個位置

        if next_row >= 橫排數:
            合併方塊()
            消方塊()
            break
        elif Game.棋盤[next_row][next_col]:
            合併方塊()
            消方塊()
            break
        else:
            Game.方塊位置 = 下個位置
                        
if __name__ == '__main__':
    設定()
    繪圖()

    按鍵 = ''
    while 按鍵 != 'q':
        按鍵 = getwch()
        if 按鍵 == '4':
            左移方塊()
        elif 按鍵 == '6':
            右移方塊()
        elif 按鍵 == '5':
            下移方塊()
        elif 按鍵 == ' ':
            直接落下方塊()

        繪圖()

    
    print("下次再來玩!")
    
    

