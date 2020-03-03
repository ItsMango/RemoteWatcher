################################################
# a new class inherit 'cls_socket' & 'threading'
#
#
# for reading data from client
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
            while not self.thread_exit_flag:  # Looping: wait for connect
                # get socket file description
                read_list, write_list, error_list = select([self.server_socket], [self.server_socket], [self.server_socket], 1)
                print(">>> ClsServerThread_2: read:{}, write:{}, error_list:{}".format(read_list, write_list, error_list))
                # processing read_list
                for sock in read_list:  # should only have one sokcet
                    client_sock, client_addr = sock.accept()
                    try:
                        while not self.thread_exit_flag:  # Looping: wait finish data processing
                            data = client_sock.recv(BUF_SIZE)
                            if data:
                                print("---> ServerThread_2收到数据: {}".format(data))
                            else:
                                print("---> ServerThread_2: 无数据, 断开")
                                break
                    finally:
                        client_sock.close()
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
    print("### Here is ServerThread module_2 ###")
    print("#####################################")    


