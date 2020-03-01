###########################
# TCP Thread module 1
###########################

import socket
import threading
import time
import select

BUF_SIZE = 2048

class ServerThread(threading.Thread):
    def __init__(self, addr):
        threading.Thread.__init__(self)
        self.server_addr = addr
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.thread_exit_flag = False

    def initServer(self):
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(self.server_addr)
        self.server_socket.listen(1)
        print(">>> ServerThread_1: 服务器已启动, 监听%d端口"%(self.server_addr[1]))

    def run(self):
        try:
            while not self.thread_exit_flag:
                read_list, write_list, error_list = select.select([self.server_socket], [self.server_socket], [self.server_socket], 1)
                print("read:{}, write:{}, error_list:{}".format(read_list, write_list, error_list))

                time.sleep(5)
                for sock in read_list:
                    client_socket, client_addr = sock.accept()  # block
                    print(">>> get data: {}".format(client_socket.recv(1024)))
                    print(">>> now! close")
                    time.sleep(5)
                    client_socket.close()
                    print(">>> close one socket")
                '''
                print(">>> ServerThread_1: 等待连接...")
                # will block
                client_socket, client_addr = self.server_socket.accept()
                print(">>> ServerThread_1: 已与{}连接".format(client_addr))
                try:
                    while not self.thread_exit_flag:
                        # will block
                        data = client_socket.recv(BUF_SIZE)
                        if data:
                            print("---> ServerThread_1收到数据: {}".format(data))
                        else:
                            print("---> ServerThread_1: 无数据, 断开")
                            break
                finally:
                    client_socket.close()
                '''
        finally:
            self.server_socket.close()
        print(">>>  ServerThread_1: End of run()")

    def disconnectServer(self):
        self.thread_exit_flag = True
        print(">>> ServerThread_1: 推出线程")



if __name__ == "__main__":
    pass
else:
    print("### Here is ServerThreadModule_1 ###")




