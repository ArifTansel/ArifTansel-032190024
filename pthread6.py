import threading
import time
import queue

counter = 0

def do_some_thing(q):
    global counter #her threadin erişebildiği bir değere eriş
    counter += 1 
    print(f"\n Job {counter} started\t thread:{threading.current_thread().name}")
    time.sleep(1)
    print(f"\n Job {counter} finished\t thread:{threading.current_thread().name}")
    q.put(counter) #queue'nin içerisine oluşan değeri at

q = queue.Queue() #oluşturulan değerleri depolamak için bir queue yapısı oluştur
threads = [] #threadleri depolamak için
#threadleri oluştur ve başlat
for _ in range(5):
    thread = threading.Thread(target=do_some_thing, args=(q,))
    threads.append(thread)
    thread.start()
#threadlerin bitmesini beklemek için kullanılır main fonksiyonumuz başlatılan threadler bitmeden devam etmez
for thread in threads:
    thread.join()
#q nun içerisindeki her değeri yaz.
while not q.empty():
    result = q.get()
    print(f"Result: {result}")