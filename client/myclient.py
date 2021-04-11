#! /usr/bin/env python3
# -*- coding:utf-8 -*-  

from socket import * 
import threading
import time

def main():     
    # 1.创建socket    
    client_socket = socket(AF_INET, SOCK_STREAM)  
    
    # 2.指定服务器的地址和端口号    
    server_addr = ('192.168.1.10',7654)
    client_socket.connect(server_addr)
    
    print('connect %s success' % str(server_addr))
    
    # 将 read_server 函数以多线程的方式启动，这样该函数（包含死循环）能与下面的死循环并发执行
    # threading.Thread(target=read_server, args=(client_socket,)).start()
    
    while True:
        # 3.给用户提示，让用户输入要检索的资料  
        send_data = input('>>')
        # 退出
        if send_data == 'quit':
            client_socket.send(send_data.encode('UTF-8'))
            break
            
        # 向服务器请求数据
        client_socket.send(send_data.encode('UTF-8'))
        
        # 从服务器接收数据
        recv_data = client_socket.recv(1024).decode('UTF-8')
        if recv_data is not None:
            print(recv_data)
        
    # 4.关闭套接字
    client_socket.close()
    
if __name__ == "__main__":
    main()

