# Task 8: Threading
# Write a Python program that:
# - Defines a function print_numbers() that prints numbers from 1 to 10, with a 1-second delay between each number.
# - Creates two threads that run the print_numbers() function concurrently.
# - Print a message indicating when both threads have finished executing.
# - Use the threading module to implement this task.
import time
import threading

class Thread(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
    
    def run(self):
        self.print_numbers()

    def print_numbers(self):
        for i in range(1, 11):
            print(i)
            time.sleep(1)


first_thread = Thread(1)
second_thread = Thread(2)

first_thread.start()
second_thread.start()

first_thread.join()
second_thread.join()

print("End")
