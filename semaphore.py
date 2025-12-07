import threading
import time

examinationroom = threading.Semaphore(1)

def enter_examinationroom(num):
    print(f"Patient {num} is waiting for his turn")
    
    examinationroom.acquire()
    print(f"Patient {num} is in the examination room")
    time.sleep(2)
    print(f"Patient {num} has left the examination room")
    examinationroom.release()

patients = []
for i in range(10):
    t = threading.Thread(target=enter_examinationroom, args=(i,))
    patients.append(t)
    t.start()

for t in patients:
    t.join()

