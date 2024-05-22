import mmap
import posix_ipc
SHMOBJ_PATH = "/foo1423"
# Paylaşılan bellek nesnesine bağlanılıyor
shm = posix_ipc.SharedMemory(SHMOBJ_PATH, posix_ipc.O_CREAT)
try :
    # Paylaşılan bellek nesnesine bağlanılıyor mmap belirlenen size kadar olamasını sağlar 
    shared_msg = mmap.mmap(shm.fd, shm.size)
    #değeri oku ve decode et byte veri gelir
    received_msg = shared_msg.read().decode()

    print(received_msg)

except ValueError : #eğer bellek boşsa unlink() edildiyse.
    print("Memory is empty")