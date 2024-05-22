import posix_ipc
import sys

#for posic_ipc doc  https://github.com/osvenskan/posix_ipc/blob/develop/USAGE.md

# mesaj kuyruğu adını belirle
queue_name = "/my_message_queue"

# Var olan bir kuyruğa bağlan
mq = posix_ipc.MessageQueue(queue_name)

#bağlanılan queue'nin özellikleri 
print("Queue {} : stores at most {} messages - large at most {} bytes each - currently holds {}".format(mq.name,mq.max_messages,mq.max_message_size,mq.current_messages))

# mesajı ve öncelik değerini al oncelik değerine göre alır 
message, priority = mq.receive()

#mesaj byte şeklinde gelir decode etmelisin
print("Alınan Mesaj:", message.decode())

# Kuyruğu kapat
mq.close()
