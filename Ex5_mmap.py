import mmap

with open("example.txt" , "w") as f :
    print("hello world",file=f)
with open("example.txt" , "r+b" ) as f :

    mmapped_file = mmap.mmap(fileno=f.fileno(),length=14 )
    print(mmapped_file.read())