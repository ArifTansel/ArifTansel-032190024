import posix_ipc
import os
import time

SEM_NAME = "/vik"


i = 0
    
#semaphore' oluştur
mutex = posix_ipc.Semaphore(SEM_NAME, posix_ipc.O_CREAT, initial_value=1)

while i < 10:
    with mutex:
        t0 = time.time()
        print(f"Process A enters the critical section at {t0}")
        t1 = time.time()
        print(f"Process A leaves the critical section at {t1}")
    i += 1
    time.sleep(3)


