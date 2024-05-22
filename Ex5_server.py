import mmap
import random
import posix_ipc
SHMOBJ_PATH = "/foo1423"
MAX_MSG_LENGTH = 50
TYPES = 8
# Paylaşılan bellek nesnesi oluşturuluyor
shm = posix_ipc.SharedMemory(SHMOBJ_PATH, posix_ipc.O_CREAT, size=MAX_MSG_LENGTH)

# Paylaşılan bellek nesnesine bağlanılıyor
memory_map = mmap.mmap(shm.fd, shm.size)

# Mesaj üretiliyor ve paylaşılan bellek nesnesine yazılıyor 0 ile type arasında bir sayı seç
shared_msg_type = random.randint(0, TYPES - 1)
#mesajı oluşturur
shared_msg_content = "My message, type {}, num {}".format(shared_msg_type, random.randint(0, 1000))
#belirlenen bellek nesnesine yazılıyor.
memory_map.write(shared_msg_content.encode())

print(f"Shared memory segment allocated correctly ({shm.size} bytes).")
print(f"Message written: {shared_msg_content}")

# Paylaşılan bellek nesnesinden bağlantı kapatılıyor
memory_map.close()
#paylaşılan belleği siler çalıştırırsan clientten alamazsın
#shm.unlink()