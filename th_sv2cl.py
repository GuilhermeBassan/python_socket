import socket
#import sys
#import time
import logging
import threading
from _thread import *

def print_debug(message):
    print(message)
    return 0

def debug_log(message):
    msg = ('\n\n\n**************************************************\n\n' +
           message +
           '\n\n**************************************************\n\n\n')
    logging.error(msg, exc_info = True)
    return 0

#socket.setdefaulttimeout(30)

try:
    print_lock = threading.Lock()

except:
    debug_log('Erro definindo objeto thread')
    exit()
    
print_debug('Objeto thread definido')

"""*****************************************************************************

                        INITIALIZING THREADED ROUTINE
        
*****************************************************************************"""
try:
    def threaded(c, packet):
    
        while True:
    
            #print_debug(packet)

            try:
                c.send(packet)
        
            except:
                debug_log('Erro no envio')
                c.close()
                exit()
                
except:
    debug_log('Erro definindo função thread')
    exit()
        
print_debug('Função thread definida')

"""*****************************************************************************

                        INITIALIZING MAIN ROUTINE
        
*****************************************************************************"""
def Main():
    
    CL_HOST = '169.254.1.1'
    CL_PORT = 2101
    cl_addr = ((CL_HOST, CL_PORT))

    SV_HOST = ''
    SV_PORT = 5000
    sv_addr = ((SV_HOST, SV_PORT))

    try:
        print_debug('Iniciando socket cliente')
        cl_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM)
        cl_socket.connect(cl_addr)
    
    except:
        debug_log('Falha na criação do socket cliente')
        exit()

    print_debug('Socket cliente estabelecido')

    try:
        print_debug('Iniciando socket servidor')
        sv_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM)
        sv_socket.bind(sv_addr)
        sv_socket.listen(5)

    except:
        debug_log('Falha na criação do socket servidor')
        exit()

    print_debug('Socket servidor estabelecido')

    while True:
        
        packet = (cl_socket.recv(1024)).encode()
        
        try:
            print('Esperando por conexão')
            conn, client = sv_socket.accept()
            print_lock.acquire()
        
        except:
            debug_log('Falha de conexão com o cliente')
            sv_socket.close()
            exit()
        
        cl_IP = client[0]
        cl_PORT = client[1]
        print('Cliente conectado: {}|{}'.format(cl_IP, cl_PORT))
        
        try:
            start_new_thread(threaded,(conn, packet))
        
        except:
            debug_log('Erro criando thread do cliente')
            sv_socket.close()
            exit()
            
        print_debug('Thread de cliente estabelecido')
    
    sv_socket.close()

if __name__ == '__main__':
    Main()
