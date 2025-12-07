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

Patient = []
for i in range(১০):
    t = threading.Thread(target=enter_examinationroom, args=(i,))
    Patient.append(t)
    t.start()

for t in Patient:
    t.join()
