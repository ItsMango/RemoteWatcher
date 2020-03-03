################################################
# a new class inherit 'cls_socket' & 'threading'
#
# for writing data to client 
# 
################################################

import threading
from select import select
import time
import cls_socket


BUF_SIZE = 2048
PROCESS_DELAY = 0.2


class ClsServerThread(threading.Thread, cls_socket.ClsSocket):
    def __init__(self, port):
        threading.Thread.__init__(self)
        cls_socket.ClsSocket.__init__(self, port)
        self. thread_exit_flag = False

    def run(self):
        self.initServer()

        try:
            #accept_flag = False
            #client_sock, client_addr = None, None
            rlist, wlist, xlist = [], [], []
            rlist.append(self.server_socket)
            xlist.append(self.server_socket)
            while not self.thread_exit_flag:  # Looping: wait for connect
                
                # get socket file description
                read_list, write_list, error_list = select(rlist, wlist, xlist, 1)
                print(">>> ClsServerThread_1: read:{}, write:{}, error_list:{}".format(read_list, write_list, error_list))
                # processing read_list & write_list
                '''
                for sock in read_list:
                    print(">>> ClsServerThread_1: read try to accept")
                    client_sock, client_addr = sock.accept()
                    print(">>> ClsServerThread_1: ({}) ({})".format(client_sock, client_addr))
                    
                    print(">>> ClsServerThread_1: get data, {}".format(client_sock.recv(BUF_SIZE)))  # 这里无法发送
                    #client_sock.send("Aloha~, {}".format(time.ctime()))
                    print(">>> ClsServerThread_1: get data, {}".format(client_sock.recv(BUF_SIZE)))

                    read_list, write_list, error_list = select([self.server_socket], [self.server_socket], [self.server_socket], 1)
                    print(">>> ClsServerThread_1: read:{}, write:{}, error_list:{}".format(read_list, write_list, error_list))
                '''
                for sock in read_list:
                    if sock is self.server_socket:
                        client_sock, client_addr = sock.accept()
                        wlist.append(client_sock)
                        xlist.append(client_sock)
                        print(">>> ClsServerThread_1: socket accept")
                        print(">>> ClsServerThread_1: {}".format(wlist))

                for sock in write_list:  # should only have one sokcet
                    try:
                        while not self.thread_exit_flag:  # Looping: wait finish data processing
                            #read_list, write_list, error_list = select(rlist, wlist, xlist, 1)
                            #print(">>> ClsServerThread_1: read:{}, write:{}, error_list:{}".format(read_list, write_list, error_list))
                            try:
                                sock.send("Aloha~, {}".format(time.ctime()).encode())
                                print(">>> ClsServerThread_1: send 'Aloha~'")
                                time.sleep(2)
                            except ConnectionAbortedError:  # catch "Client disconnect error"
                                # 客户端断开连接
                                print(">>> ClsServerThread_1: client disconnet, remove 'sock'")
                                wlist.remove(sock)
                                time.sleep(0.5)
                                break
                    finally:
                        sock.close()
                    
                # time delay
                time.sleep(PROCESS_DELAY)
        finally:
            self.disconnetServer()

    def stopServerThread(self):
        self.thread_exit_flag = True



if __name__ == "__main__":
    pass
else:
    print("#####################################")
    print("### Here is ServerThread module_1 ###")
    print("#####################################")



