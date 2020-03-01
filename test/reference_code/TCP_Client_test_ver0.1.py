from socket import *


SERVER_ADDR = (('127.0.0.1', 6060))

if __name__ == "__main__":
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.connect(SERVER_ADDR)


    while True:
        data = input("> input something: ")
        if not data:
            break

        # send data
        server_socket.send(data.encode('utf-8'))
    
    server_socket.close()
    print(">>> Client close...")





