from socket import AF_INET, SOCK_STREAM, socket
from time import sleep
from select import select
from msvcrt import kbhit , getwch, getwche, putwch
import sys


DEFAULT_HOST = '127.0.0.1'

#主機ip
target_host = DEFAULT_HOST


LOGS_SIZE = 20

#聊天紀錄
chat_logs = []

#輸入字視
input_chars = []


def make_server_and_wait(host):
    main_socket = socket(AF_INET, SOCK_STREAM)
    main_socket.bind((host, 50007))
    main_socket.listen(1)

    print('迷你聊天程式 (伺服器:', host,') . 等待連線中...\n\n')

    #conn是網路端點
    conn, addr =  main_socket.accept()
    conn.setblocking(False)

    print('已連接 by ', addr)
    return conn

    
def make_client_and_connect(host):
    conn =  socket(AF_INET, SOCK_STREAM)
    print('準備連接到... ', host, ' ' , 50007)
    conn.connect((host, 50007))
    conn.setblocking(False)
    return conn
    


def add_chat_log(str):
    if len(chat_logs) == LOGS_SIZE:
        chat_logs.pop(0)
    
    chat_logs.append(str)

def draw_chat():
    print('\n'*25)
    
    for log in chat_logs:
        print(log)
        
    tmp = '=============網路聊天程式 (伺服器 {})====ESC 離開=========='
    print(tmp.format(target_host))
    
    for c in input_chars:
        putwch(c)





        
if __name__ == '__main__':        
 


    if len(sys.argv) == 3:
        target_host = sys.argv[2]
        
    if sys.argv[1] == 'server':
        conn = make_server_and_wait(target_host)
    elif sys.argv[1] == 'client':
        conn = make_client_and_connect(target_host)
    else:
        print("用法 : python net_chat.py  [server/client]  [ip]")
        
        sys.exit()
        
    
        
    sleep(1)
    draw_chat()

    
    while True:
        
        read_list, _ , _ = select([conn],[],[],0)

        if read_list:
            net_data = conn.recv(1024)
            if not net_data:
                print("網路已中斷...")
                break
            add_chat_log('<---別人回答: ' + net_data.decode())
            draw_chat()
            

        if kbhit():
            c = getwch()
            if c == '\x1b':
                #按ESC 離開
                print("中斷連線 跳出程式")
                break
            elif c == '\r': #按enter
                if input_chars:
                    temp_s = ''
                    for temp_c in input_chars:
                        temp_s = temp_s + temp_c
                    conn.send(temp_s.encode())
                    add_chat_log('自己的話--->  ' +  temp_s)
                
                input_chars = []
            elif c == '\x08':
                #Backspace 被按了
                if input_chars:
                    input_chars.pop()

            else:
                input_chars.append(c)

            draw_chat()
        
        sleep(0.1)
     


