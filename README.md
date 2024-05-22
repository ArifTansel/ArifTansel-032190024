Basit Threading algoritmaları:

Kullanılan kütüphaneler : Threading, Time, Posix_ipc, mmap

## Ex1 
 Her biri farklı bir mesajı içeren paralel thread yapısı oluşturur

## Ex2 
 Her biri farklı bir mesajı ve kümülatif bir toplamı içeren beş ayrı thread oluşturup çalıştırarak, threadlerin paralel olarak çalışmasını gösterir.

## Ex3 
 Bir message queue oluşturulur ve farklı processlerde okuma ve yazma işlemeleri yapılır

## Ex5 :
    mmap : mmap bellek üzerinde işlemler yapmayı kolaylaştırır bir dosyayı belleğe yükleyip işlemler yapma gibi özellikleri vardır
    daha fazla için :
        https://docs.python.org/3/library/mmap.html
    server : SharedMemory yapısıyla belirli uzunlukta farklı processlerin erişebileceği bir bellek adresi oluşturur bu bellek bellek adresine mmap ile bir veri yazılır.
    client : Eklenen bir veriyi okuma işlemi yapılır.

## Ex6 :
    Bir Semaphore oluşturulur bu semaphore ile kritik bölgesine giren processlerin farklı zaman aralıklarında çalışması sağlanır initial_value değeri kaç processin birlikte girebileceğini belirtir.

