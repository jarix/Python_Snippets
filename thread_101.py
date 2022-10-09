# -*- coding: utf-8 -*-
"""
    Thread 101

    Simple examples how to use Python Threads.

    Author: Jari Honkanen
"""

from datetime import datetime
from threading import Thread
import time
 

def display_time(thread_name, sleep_time):
    """ Loop with delay and display current time """
    print(thread_name + " starting ...")
    count = 0
    while count < 6:
        time.sleep(sleep_time)
        print(f"Iteration {count}: {thread_name}: Time = {datetime.now().time()}")
        count += 1

    print(thread_name + " exiting ...")


if __name__ == "__main__":

    print("Thread 101")

    # Instantiate a few Threads
    thread_1 = Thread(target=display_time, args=("Thread_1", 1))
    thread_2 = Thread(target=display_time, args=("Thread_2", 1.5))
    thread_3 = Thread(target=display_time, args=("Thread_3", 2))

    # Start the Threads
    thread_1.start()
    thread_2.start()
    thread_3.start()

    print("Main exiting ...")
