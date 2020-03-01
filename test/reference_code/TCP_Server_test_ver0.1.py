from socket import *



HOST = '127.0.0.1'  # localhost
PORT = 6060
SERVER_ADDR = (HOST, PORT)

BUF_SIZE = 1024


if __name__ == "__main__":
    server_socket = socket(AF_INET, SOCK_STREAM)  # AF_INET: IPv4  SOCK_STREAM: TCP
    print(server_socket.bind(SERVER_ADDR))
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.listen(2)
    print(">>> 服务器已启动, 监听%d端口" % (SERVER_ADDR[1]))

    try: # 管理关闭server socket的循环
        while True:
            print(">>> 等待Client连接...")
            client_socket, client_addr = server_socket.accept()
            print(">>> Client已连接, {}".format(client_addr))

            try: # 管理关闭已连接的client socket的循环
                while True:
                    data = client_socket.recv(2048)  # 阻塞  数据按byte接收??????
                    if data:
                        print(">>> 收到数据: {}".format(data.decode("utf-8")))
                    else:
                        print(">>> 无数据, Client已断开")
                        break
            finally:
                client_socket.close()
    finally:
        server_socket.close()





