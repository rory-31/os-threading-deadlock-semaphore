import threading
import time

resource_a = threading.Lock()
resource_b = threading.Lock()

def thread_function_1():
    with resource_a:
        print("Thread 1 acquired resource A")
        time.sleep(1)

        with resource_b:
            print("Thread 1 acquired resource B")

def thread_function_2():
    with resource_a:
        print("Thread 2 acquired resource A")
        time.sleep(1)

        with resource_b:
            print("Thread 2 acquired resource B")

t1 = threading.Thread(target=thread_function_1)
t2 = threading.Thread(target=thread_function_2)

t1.start()
t2.start()

t1.join()
t2.join()
