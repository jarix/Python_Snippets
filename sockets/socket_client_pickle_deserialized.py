# -*- coding: utf-8 -*-
"""
    Socket client example with pickle deserialization
    Runs in localhost with socket_server_pickle_serialized.py

    Author: Jari Honkanen

"""
import socket
import pickle

PORT_NUMBER = 8554
HEADER_SIZE = 10
BUFFER_SIZE = 16

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), PORT_NUMBER))

while True:

    rx_msg = b''
    new_msg = True

    while True:
        msg = s.recv(BUFFER_SIZE)
        if new_msg:
            print(f"New message length: {msg[:HEADER_SIZE]}")
            msg_len = int(msg[:HEADER_SIZE])
            new_msg = False

        rx_msg += msg

        if len(rx_msg) - HEADER_SIZE == msg_len:
            print("Complete pickled dictionary Message received.")
            rx_data = pickle.loads(rx_msg[HEADER_SIZE:])
            print("Received dictionary:")
            print(rx_data)

            rx_msg = b''
            new_msg = True

    print("Received Serialized Message:")
    print(rx_msg)