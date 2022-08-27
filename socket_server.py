#!/usr/bin/env python3
import threading
import socket


def image_getter_server():
    # host = socket.gethostname()
    host = '0.0.0.0'
    port = 9000

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together
    server_socket.listen(2)
    print('Server started')

    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        with open('Image.jpeg', '+wb') as file:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                file.write(data)
        print("Data received")
        conn.send(b'ACK')
        conn.close()


if __name__ == '__main__':
    image_getter_server()
