#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from multiprocessing import Process
import threading
from socket import *
import RPi.GPIO as gpio

# 设置IP地址和端口
my_addr = ('192.168.1.10', 7654)

# 该函数需要为客户端提供服务
def do_service(connect_socket): 
    while True:
        recv_data = connect_socket.recv(1024).decode('UTF-8')
        # 打印接收的数据
        print('recv:',recv_data)
        
        if len(recv_data) == 0:
            # 发送方关闭tcp的连接,recv()不会阻塞，而是直接返回''
            print('client %s close' % str(client_addr))                
            # s.getpeername()   s.getsockname()            
            gpio.output(17,gpio.LOW)            
            print('client %s is closed' % str(connect_socket.getpeername()))            
            break
        
        if ((len(recv_data) == 1) and (recv_data[0] == '1')):
            gpio.output(17,gpio.HIGH) # 灯亮
            print('灯亮')
        else:
            gpio.output(17,gpio.LOW)
            print('灯灭')  

        # 返回接收的数据
        connect_socket.send(recv_data.encode())
        
def main():
    # 0.init gpio
    # 设置GPIO编号为bcm方式
    gpio.setmode(gpio.BCM)
    gpio.setup(17,gpio.OUT)
    
    # 1.创建socket
    # stream流式套接字,对应tcp
    listen_socket = socket(AF_INET, SOCK_STREAM)
    
    # 设置允许复用地址,当建立连接之后服务器先关闭，设置地址复用    
    # 设置socket层属性    复用地址，不用等2msl，    允许    
    listen_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  
    
    # 2.绑定端口
    listen_socket.bind(my_addr)
    
    # 3，接听状态
    # 定义最多能挂起的数目,允许两个客户端等待发送信息（挂起）
    # 设置套接字成监听,4表示一个己连接队列长度
    listen_socket.listen(4)
    print('listening...')
    
    # 4.等待客户端来请求
    # 父进程只专注接受连接请求
    while True:
        # 接受连接请求，创建连接套接字，用于客户端间通信
        # accept默认会引起阻塞
        # 新创建连接用的socket, 客户端的地址
        connect_socket, client_addr = listen_socket.accept()
        
        # print(connect_socket)        
        print('seccess',client_addr,'\n') 

        # 每当来新的客户端连接，创建子进程，由子进程和客户端通信        
        process_do_service = Process(target=do_service, args=(connect_socket,))        
        process_do_service.start()         
        
        # 父进程，关闭connect_socket        
        connect_socket.close()
        
    # 恢复所有使用过的通道状态为输入，
    # gpio.cleanup()
        
if __name__ == "__main__":   
    main()
    