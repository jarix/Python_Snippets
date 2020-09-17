# -*- coding: utf-8 -*-
"""
    Socket client example
    Runs in localhost with socket_server.py

    Author: Jari Honkanen

"""
import socket

PORT_NUMBER = 8554
HEADER_SIZE = 10
BUFFER_SIZE = 16

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), PORT_NUMBER))

while True:

    rx_msg = ""
    new_msg = True

    while True:
        msg = s.recv(BUFFER_SIZE)
        if new_msg:
            print(f"New message length: {msg[:HEADER_SIZE]}")
            msg_len = int(msg[:HEADER_SIZE])
            new_msg = False

        rx_msg += msg.decode("utf-8")

        if len(rx_msg) - HEADER_SIZE == msg_len:
            print("Message received:")
            print(rx_msg[HEADER_SIZE:])
            rx_msg = ""
            new_msg = True

    print(rx_msg)