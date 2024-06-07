# -*- coding: utf-8 -*-
"""
    Socket server example with data serialized with pickle
    Runs in localhost with socket_client_pickle_deserialized.py

    Author: Jari Honkanen

"""
import socket
import time
import pickle

PORT_NUMBER = 8554
HEADER_SIZE = 10

# Create a dictionary of data to send
tx_data = { "msg_type" : "Test Message",
        "msg_time" : time.time(), 
        "msg_str" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        }
        
msg = pickle.dumps(tx_data)
#print(msg)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), PORT_NUMBER))
s.listen(5)

while True:
    clientSocket, addr = s.accept()
    print("Connection from ", addr)

    msg = bytes(f"{len(msg):<{HEADER_SIZE}}", "utf-8") + msg

    clientSocket.send(msg)




