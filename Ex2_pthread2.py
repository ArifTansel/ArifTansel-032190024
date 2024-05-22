import threading
import time
class ThreadData :
    def __init__(self,thread_id,sum,message) : #Threadlerimiz için data class ı oluştur içerisinde mesaj sum ve threadId değişkenleri olsun
        self.threadId = thread_id
        self.sum = sum
        self.message = message


def print_hello(threadData : ThreadData) : # threadlerin çalıştıracağı fonksiyonlar
    time.sleep(1) # paralel çalışmayı görmemiz için bekleme 
    print("thread {}: {} Sum={}".format(threadData.threadId,threadData.message,threadData.sum)) # verilen threadData verilerini bas
if __name__ == "__main__" :
    threads = [] #threadlerin depolanması için array oluştur
    messages=["English: Hello World!",
    "German: Guten Tag, Welt!",
    "French: Bonjour, le monde!",
    "Spanish: Hola al mundo",
    "Klingon: Nuq neH!"] # ekrana yazdırmak için mesajlarımız
    sum = 0 
    for index , message in enumerate(messages) : # her mesaj için index numarasını ve mesajı al
        sum +=index # index numarasını artırarak git
        t_data = ThreadData(index,sum,message) # bir sınıf içerisinde index , sum , mesaj verilerini koy
        t = threading.Thread(target = print_hello,args=(t_data,)) # ThreadData ile print_hello fonksiyonunu çalıştıracak bir thread örneği oluştur
        threads.append(t) #threads arrayinin içerisine at
    for i in threads :
        i.start() # her thread için threadleri başlat