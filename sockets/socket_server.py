# -*- coding: utf-8 -*-
"""
    Socket server example
    Runs in localhost with socket_client.py

    Author: Jari Honkanen

"""
import socket
import time

PORT_NUMBER = 8554
HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), PORT_NUMBER))
s.listen(5)

while True:
    clientSocket, addr = s.accept()
    print("Connection from ", addr)

    msg = "Welcome to the socket server! -- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    msg = f"{len(msg):<{HEADER_SIZE}}" + msg

    clientSocket.send(msg.encode(encoding="UTF-8", errors="strict"))

    while True:
        time.sleep(2)
        msg = f"The current time is {time.time()}"
        msg = f"{len(msg):<{HEADER_SIZE}}" + msg

        clientSocket.send(msg.encode(encoding="UTF-8", errors="strict"))


