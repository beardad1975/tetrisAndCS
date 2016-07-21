import socket

主機 = '127.0.0.1'
埠號 = 50007

print("準備連線到...", 主機, ":",埠號) 

網路端點 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
網路端點.connect((主機, 埠號))

print("連線成功")

while True:
    content = input("輸入要傳送的字(按q離開): ")
    if content == 'q':
        print("中斷連線...")
        break
    網路端點.sendall(content.encode())
   
網路端點.close()    
   
