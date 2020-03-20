#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:00:18 2020

@author: root
"""

import socket

from _thread import *
import threading

print_lock = threading.Lock()

def threaded(c):
    
    while True:
        
        c.send('Hello!'.encode())
        data = c.recv(1024)
        
        if not data:
            print('Bye.')
            print_lock.release()
            break
        
        data = data[::-1]
        c.send(data)
        
    c.close()
    
def Main():
    
    host = ''
    port = 12345
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    
    s.listen(5)
    
    while True:
        
        c, addr = s.accept()
        print_lock.acquire()
        print('Connected to {}:{}'.format(addr[0],addr[1]))
        
        start_new_thread(threaded, (c,))
        
    s.close()
    
if __name__ == '__main__':
    Main()