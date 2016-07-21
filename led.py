
from serial import Serial
from time import sleep

conn = Serial("com23",38400)

num = [1,2,4,8,16,32,64,128]

sleep(4)

conn.write(bytes(num))



