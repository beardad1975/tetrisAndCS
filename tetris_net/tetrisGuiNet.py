from block import T_Shape,O_Shape,I_Shape,L_Shape,J_Shape,S_Shape,Z_Shape
from copy import deepcopy
from msvcrt import getwch, kbhit
from time import time, sleep
from random import choice, randrange
from tkinter.messagebox import showinfo
from tkinter import *

from socket import AF_INET, SOCK_STREAM, socket

import _thread
import queue
import struct
import json
from time import sleep
from select import select


class GameGui(Frame):
    color_list = ['black', 'red', 'yellow', 'gold', 'orange',
                      'green2', 'cyan','VioletRed1', 'white']

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
            
        self.id = self.after(2000, self.period)

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
                    label.config(bg=self.color_list[col],relief=RAISED)
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

    def onLeftKey(self, event):
        self.moveLeft()
        self.draw()
        net_tetris.to_outQueue()

    def onRightKey(self, event):
        self.moveRight()
        self.draw() 
        net_tetris.to_outQueue()

    def onBottomKey(self, event):
        self.moveBottom()
        self.draw()
        net_tetris.to_outQueue()

    def onDownKey(self, event):
        self.moveDown()
        self.draw()
        net_tetris.to_outQueue()

    def onTurnKey(self, event):
        self.turnClockwise()
        self.draw() 
        net_tetris.to_outQueue()
        
    def onTurnCounterKey(self, event):
        self.turnCounter()
        self.draw()
        net_tetris.to_outQueue()
        
        
    def period(self):
        self.moveDown()
        self.draw()
        net_tetris.to_outQueue()
        
        self.after_id = self.after(2000, self.period)
        
            
            
class GameGuiNet(GameGui):
    def __init__(self, player_game, net_type, host, parent,title):
        GameGui.__init__(self, player_game.row_size, player_game.col_size,parent,title)
        self.player_game = player_game
        self.outQueue = queue.Queue()
        self.inQueue = queue.Queue()
        self.host = host
        
        self.block = None
        self.previous_board = None
        
        if net_type == "server":
            self.make_server_and_wait()
        elif net_type == "client":
            self.make_client_and_connect()
        else:
            print("net_type must server or client")
            sys.exit()
        
        self.net_type = net_type
        
        self.make_thread()
        self.to_outQueue()
        self.from_inQueue()
    
    def period(self):
        pass
        
    def make_server_and_wait(self):
        main_socket = socket(AF_INET, SOCK_STREAM)
        main_socket.bind((self.host, 50007))
        main_socket.listen(1)

        print('mini tetris server at ', self.host,' . Waiting for connect...\n\n')

        conn, addr =  main_socket.accept()
        self.conn = conn
        self.conn.setblocking(False)

        print('Connected by ', addr)

    def make_client_and_connect(self):
        self.conn =  socket(AF_INET, SOCK_STREAM)
        print('connect to ', self.host, ' ' , 50007)
        self.conn.connect((self.host, 50007))
        self.conn.setblocking(False)

    def make_thread(self):
        _thread.start_new_thread(self.net_thread, ())
    
    def net_thread(self):
        self.remain_size = 0
        self.remain_data = b''
        self.chuck = b''
        
        self.net_board_data = b''
        while True:
            
            readable, _ , _ = select([self.conn],[],[],0)

            if readable:
                self.chuck = self.conn.recv(4096)
                if not self.chuck:
                    print('connection closed')
                    sys.exit()
            
                self.remain_data += self.chuck

                
                #print('chuck--> ',chuck)
                #print('remain_data--> ',remain_data)

            ###handle another new net_board_data
            if self.remain_size == 0:
                
                if len(self.remain_data) > 4:
                    self.length_buf = self.remain_data[:4]
                    self.remain_data = self.remain_data[4:]
                    self.remain_size = struct.unpack('!I', self.length_buf)[0]
                    #print('length_buf-->', length_buf)
                    #print('remain_size-->', remain_size)
                    
            ### handle resemble net board data
            if self.remain_size > 0:
                if self.remain_size > len(self.remain_data):
                    self.net_board_data  += self.remain_data
                    self.remain_size -= len(self.remain_data)
                    self.remain_data = b''
                    
                    
                        #bingo . get 1 net board data 
                        

                else:
                    #remain_size <= len(remain_data)
                    self.net_board_data += self.remain_data[:self.remain_size]
                    
                    self.remain_data = self.remain_data[self.remain_size:]
                    self.remain_size = 0
                    
                    #net_board_data done
                    #print (net_board_data)
                    
                    dic = json.loads(self.net_board_data.decode())
                    #dic = pickle.loads(net_board_data)
                    #print('Got one dic-->\n')
                    #print('-------------')
                    self.net_board_data = b''
                    
                    self.inQueue.put(dic)
            elif self.remain_size < 0:
                print('error: remain_size should not negetive')
                 

            #print('chuck size: ' , len(chuck),'len(remain_data): ', len(remain_data), ' remain size:' , remain_size )    
            #print('Press Any Key.....')
            #getwch()
            
            ###handle net out queue
            try:
                out_dic = self.outQueue.get(block=False)
            except queue.Empty:
                pass
            else:
                 #prepare dict of board and block
                
                tmp_net_data = json.dumps(out_dic).encode()
                #net_board_data = pickle.dumps(dic)
                length = struct.pack('!I',len(tmp_net_data))
                packet = length + tmp_net_data
                
                self.conn.sendall(packet)
                #print('send one dic')                
            
            sleep(0.05)        

    def to_outQueue(self):
        tmp_board = deepcopy(self.player_game.board) 
        if self.player_game.block:
            all_pos = self.player_game.block.tellAllPos()
            for row, col in all_pos:
                tmp_board[row][col] = self.player_game.block.color_num
    
    
        if not tmp_board == self.previous_board:
            out_dic = {}
            out_dic['board'] = tmp_board
            #dic['block'] = tetris.block
            out_dic['score'] = self.player_game.score
          
            #out_dic['ref_pos'] = self.player_game.block.ref_pos
            #out_dic['turn_type'] = self.player_game.block.turn_type
            #out_dic['turn_delta'] = self.player_game.block.turn_delta
            #out_dic['color_num'] = self.player_game.block.color_num
            #out_dic['block_type'] = self.player_game.block.block_type
            
            #print('out_dic--> ', out_dic)
            self.outQueue.put(out_dic)
            self.previous_board = tmp_board

        
        
    def from_inQueue(self):
        try:
            in_dic = self.inQueue.get(block=False)
        except queue.Empty:
            #print('No in queue...')
            pass
        else:
            self.board = in_dic['board']
            #tetris.block = dic['block']
            self.score = in_dic['score']
            #print('in queue score: ', in_dic['score'])
            
            #self.block.ref_pos = in_dic['ref_pos']
            #self.block.turn_type = in_dic['turn_type']
            #self.block.turn_delta = in_dic['turn_delta']
            #self.block.color_num = in_dic['color_num']
            #self.block.block_type = in_dic['block_type']
            
            #print('dic : ref_pos -> ' ,dic['ref_pos'])
            #print('dic : turn_type -> ', dic['turn_type'])
            self.update_score()
            self.draw()
            self.update()

        self.after(100, self.from_inQueue)

    def draw(self):
        

        for row_index, row in enumerate(self.board):
            for col_index, col in enumerate(row) :
                if col >= 1:
                    label = self.gui_board[row_index][col_index]
                    label.config(bg=self.color_list[col],relief=RAISED)
                else:
                    label = self.gui_board[row_index][col_index]
                    label.config(bg='black',relief=GROOVE)
        self.update()

if __name__ == '__main__':
    
       
    root = Tk()

    gui_tetris1 = GameGui(20, 10,root,'我的俄羅斯方塊')




    root.bind('<Left>', gui_tetris1.onLeftKey)
    root.bind('<Right>', gui_tetris1.onRightKey)
    root.bind('<Down>', gui_tetris1.onDownKey)
    root.bind('<space>', gui_tetris1.onBottomKey)
    root.bind('<Up>', gui_tetris1.onTurnKey)

    
    net_type = sys.argv[1]
    if not net_type in ['server', 'client']:
        print("Usage: python tetrisGuiNet.py [server/client] [ip] ")
        sys.exit()
    
    host = '127.0.0.1'
    if len(sys.argv) == 3:
        host = sys.argv[2]

    net_tetris = GameGuiNet(gui_tetris1,net_type, host ,root,'別人的俄羅斯方塊')



    gui_tetris1.pack(side=LEFT)
    gui_tetris1.draw()   
    Label(root,text='',width=5).pack(side=LEFT)
    net_tetris.pack(side=LEFT)
    net_tetris.draw()    
    

    root.focus()

    root.mainloop()
    

