import os
import sys
import time
import posix_ipc
#for posic_ipc doc  https://github.com/osvenskan/posix_ipc/blob/develop/USAGE.md

# mesaj kuyruğunun adı "/" ile başlamak zorunda
queue_name = "/my_message_queue"

# Kuyruk oluştur veya var olan kuyruğa bağlan
mq = posix_ipc.MessageQueue(queue_name, posix_ipc.O_CREAT)
# Mesaj oluştur
message = "102."
#mesajı gönder öncelik sırasını belirle
mq.send(message,priority=1)

print("Mesaj gönderildi:", message)
