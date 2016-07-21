from random import randint

class Game:
    答案 = 0
    範圍 = 0

def 設定():
    
    按鍵 = input("請輸入要猜範圍: ")
    Game.範圍 = int(按鍵)
    
    Game.答案 = randint(1, Game.範圍 )

def 主迴圈():
    while True:
        s = "請輸入數字1~" + str(Game.範圍) + ": "
        按鍵 = input(s)

        按鍵_數字 = int(按鍵)

        if 按鍵_數字 > Game.答案 :
            print("太大了")
        elif 按鍵_數字 < Game.答案 :
            print("太小了")
        else:
            print("答對了")
            break

    print("遊戲結束")
    
if __name__ == "__main__":
    設定()
    主迴圈()   


    