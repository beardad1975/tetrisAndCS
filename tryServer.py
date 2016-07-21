import socket

主機 = '192.168.2.60'
埠號 = 50007

伺服端點 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
伺服端點.bind((主機, 埠號))
伺服端點.listen(1)
    
print("伺服器資訊： " , 伺服端點.getsockname())
print('等待連線中... ')
    
網路端點, addr =  伺服端點.accept()
   
print('已連線...來自 ', addr)
while True:
    net_data = 網路端點.recv(1024)
    if not net_data:
        print("連線已被中斷...")
        break   
    print('接收到: ', net_data.decode())

網路端點.close()
伺服端點.close()
