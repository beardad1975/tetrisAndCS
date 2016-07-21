
from msvcrt import getwch, kbhit
from time import time, sleep
from random import choice
from board import Board

import socket
from select import select
import json
import pickle
import struct

HOST = '127.0.0.1'
PORT = 50077

tetris = Board(20, 10)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print('mini on way tetris server. Waiting for connect...\n\n')

conn, addr =  s.accept()
conn.setblocking(False)

print('connected by ', addr)
sleep(1)

#tetris.draw()

#previous_time = time()

#key = ''

# remain 0 :receiving finished , otherwise remains
remain_size = 0
remain_data = b''
chuck = b''
#what i want 
net_board_data = b''

while True:
    
    read_list, _ , _ = select([conn],[],[],0)

    if read_list:
        chuck = conn.recv(4096)
        if not chuck:
            print('connection closed')
            break
    
        remain_data += chuck

        
        #print('chuck--> ',chuck)
        #print('remain_data--> ',remain_data)

    ###handle another new net_board_data
    if remain_size == 0:
        
        if len(remain_data) > 4:
            length_buf = remain_data[:4]
            remain_data = remain_data[4:]
            remain_size = struct.unpack('!I', length_buf)[0]
            #print('length_buf-->', length_buf)
            #print('remain_size-->', remain_size)
            
    ### handle resemble net board data
    if remain_size > 0:
        if remain_size > len(remain_data):
            net_board_data  += remain_data
            remain_size -= len(remain_data)
            remain_data = b''
            
            
                #bingo . get 1 net board data 
                

        else:
            #remain_size <= len(remain_data)
            net_board_data += remain_data[:remain_size]
            
            remain_data = remain_data[remain_size:]
            remain_size = 0
            
            #net_board_data done
            #print (net_board_data)
            dic = json.loads(net_board_data.decode())
            #dic = pickle.loads(net_board_data)
            #print('Got one dic-->\n', dic)
            #print('-------------')
            net_board_data = b''
            
            tetris.board = dic['board']
            #tetris.block = dic['block']
            tetris.score = dic['score']
            
            tetris.block.ref_pos = dic['ref_pos']
            tetris.block.turn_type = dic['turn_type']
            tetris.block.turn_delta = dic['turn_delta']
            tetris.block.color_num = dic['color_num']
            tetris.block.block_type = dic['block_type']
            
            #print('dic : ref_pos -> ' ,dic['ref_pos'])
            #print('dic : turn_type -> ', dic['turn_type'])
            tetris.draw()
    
            # tetris.draw()
    elif remain_size < 0:
        print('error: remain_size should not negetive')
         

    #print('chuck size: ' , len(chuck),'len(remain_data): ', len(remain_data), ' remain size:' , remain_size )    
    #print('Press Any Key.....')
    #getwch()
    sleep(0.1)
    

