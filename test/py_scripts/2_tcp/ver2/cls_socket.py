##############################
# a new class inherit 'socket'
#
#
# base function of socket
##############################

import socket

HOST = '192.168.3.9'

class ClsSocket():
    def __init__(self, port):
        self.server_addr = (HOST, port)  # localhost
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def initServer(self):
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(self.server_addr)
        self.server_socket.listen(1)
        print(">>> cls_socket: 服务器启动, 监听端口%d" % (self.server_addr[1]))

#    def getSocket(self):
#        return self.server_socket

    def disconnetServer(self):
        self.server_socket.close()
        print(">>> cls_socket: 服务器停止监听端口%d" % (self.server_addr[1]))






if __name__ == "__main__":
    pass
else:
    print("######################")
    print("### Using ClsSocket###")
    print("######################")


