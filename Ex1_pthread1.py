import threading
import time

def PrintHello(thread_id, message ) :
    time.sleep(3) #paralelliği görmek için bekle
    print("Thread {} : {}" .format(thread_id,message)) # thread_id ve message bas
if __name__ == "__main__" :
    messages=["English: Hello World!",
        "German: Guten Tag, Welt!",
        "French: Bonjour, le monde!",
        "Spanish: Hola al mundo",
        "Klingon: Nuq neH!"] # ekrana yazdırmak için mesajlarımız

    for thread_id , message in enumerate(messages) :
        t = threading.Thread(target = PrintHello , args=(thread_id,message)).start() #messages lardaki her message için PrintHello fonksiyonuna bir thread oluştur ve başlat