# -*- coding: utf-8 -*-
"""
    Simplest possible socket client
    Runs in localhost with socket_server_simple.py

    Author: Jari Honkanen

"""
import socket

PORT_NUMBER = 8554
RX_BUF_SIZE = 8

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), PORT_NUMBER))

rx_msg = ""

while True:
    msg = s.recv(RX_BUF_SIZE)
    if len(msg) <= 0:
        break
    rx_msg += msg.decode("utf-8")

print(rx_msg)