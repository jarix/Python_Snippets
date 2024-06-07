# -*- coding: utf-8 -*-
"""
    Simplest possible socket server
    Runs in localhost with socket_client_simple.py

    Author: Jari Honkanen

"""
import socket

PORT_NUMBER = 8554

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), PORT_NUMBER))
s.listen(5)

while True:
    clientSocket, addr = s.accept()
    print("Connection from ", addr)

    msg = "Welcome to the simple socket server!"

    clientSocket.send(msg.encode(encoding="UTF-8", errors="strict"))
    clientSocket.close()
