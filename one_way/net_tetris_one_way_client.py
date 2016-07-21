import socket
import json
import pickle
import struct

from msvcrt import getwch, kbhit
from time import time, sleep
from random import choice
from board import Board

length = b''

def net_send_board(conn, tetris):
    #準備棋盤和積木資料 board and block
    dic = {}
    dic['board'] = tetris.board
    
    dic['score'] = tetris.score
    
    dic['ref_pos'] = tetris.block.ref_pos
    dic['turn_type'] = tetris.block.turn_type
    dic['turn_delta'] = tetris.block.turn_delta
    dic['color_num'] = tetris.block.color_num
    dic['block_type'] = tetris.block.block_type
    
    net_board_data = json.dumps(dic).encode()
    #net_board_data = pickle.dumps(dic)
    length = struct.pack('!I',len(net_board_data))
    packet = length + net_board_data
    
    #傳送資料
    conn.sendall(packet)

tetris = Board(20, 10)

HOST = '127.0.0.1'
PORT = 50077

#網路端點
conn =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('連線到...', HOST, ' ' , PORT)
conn.connect((HOST, PORT))


conn.setblocking(False)


sleep(1)

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
            print("離開...")
            break

        tetris.draw()
        net_send_board(conn, tetris)

    ellapsed = time() - previous_time
    if ellapsed > 2:
        previous_time = time()
        tetris.moveDown()
        tetris.draw()
        net_send_board(conn, tetris)

    

