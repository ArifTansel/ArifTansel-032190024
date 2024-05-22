import threading
import random

NUM_THREADS = 10
ITERATIONS = 1000000

#paralel bir şekilde NUM_THREADS kadar threadi çalıştır.

def busy_work(tid): #threadlerin çalıştıracağı fonksiyon
    result = 0.0 #toplama değeri
    print(f"Thread {tid} starting...")
    for i in range(ITERATIONS): #iteration kadar dön ve rastgele bir sayıyla topla
        result += random.random()
    print(f"Thread {tid} done. Result = {result}") #ekrana çıktı ver


threads = []#threadleri depolamak için

for t in range(NUM_THREADS):
    print(f"Main: creating thread {t}") 
    # threadleri oluşturulur ve arg olarak id değeri verilir.
    thread = threading.Thread(target=busy_work, args=(t,))
    thread.start() # threadleri başlat
    threads.append(thread) #threadleri threads arrayinin içerisine at
