from socket import *
import time
s = socket(AF_INET, SOCK_STREAM)
s.bind(('',10000))
s.listen((10))
while True :
    client, addr = s.accept()
    print(client)
    print("Запрос на соединение от %s" % str(addr))
    timestr=time.ctime(time.time())+"\n"
    client.send(timestr.encode('utf-8'))
    client.close()