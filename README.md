# 網路、GUI與電子控制中的運算思維
# 以Python程式語言為例
# (主題為tetris)

2016/7/20 於大溪高中上課的程式範例與簡易說明

# 需求
python3
pyserial(用pip安裝)
使用內建msvcrt，該library只針對windows平台
(所有程式以command prompt執行)

# 猜數字
用法： python guess.py

# 命令列的迷你tetris
用法：python tetrisMini_final.py
(按鍵請看程式)

# 命令列的tetris
用法：python tetris_final.py
(按鍵請看程式)

# 矩陣LED上的tetris
(需安裝pyserial，用pip可安裝)
(要有max7219的8x8矩陣LED，並使用[ledControl](http://playground.arduino.cc/Main/LedControl)的library)
(已寫好的arduino韌體在max7219_v2資料夾內)
(com port要在程式內修改)
用法：python tetrisLed_final.py

# Gui tetris
用法：python tetrisGui_final.py 
(內容2p, 按鍵請看程式)

# 網路聊天程式
Server用法：python netChat.py server [server的ip]
client用法：python netChat.py client [server的ip] 

# 網路連線tetris(檔案在tetris_net資料夾內)
Server用法：python tetrisGuiNet.py server [server的ip]
client用法：python tetrisGuiNet.py client[server的ip]




