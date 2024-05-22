import posix_ipc
import os
import time

SEM_NAME = "/vik"

i = 0
#semaphore oluşturulur
mutex = posix_ipc.Semaphore(SEM_NAME, posix_ipc.O_CREAT, mode=0o644, initial_value=1)

#processlerin bilgi paylaşması sağlanır
for i in range(10):
    with mutex:
        t0 = time.time()
        print(f"Process B enters the critical section at {t0}")
        t1 = time.time()
        print(f"Process B leaves the critical section at {t1}")
    time.sleep(2)

# Close the semaphore
mutex.close()
#semafor silinir ve geri döndürülemez
posix_ipc.unlink_semaphore(SEM_NAME)
