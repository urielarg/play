import os
import mmap

a=1
for xxx in os.listdir("/home/ian/probanding/"):
    b="No"
    if "Player Name:" in xxx.read():
    b="Yes"
    dst = str(a) + b + ".txt"
    src ='/home/ian/probanding/'+ xxx
    dst ='/home/ian/probanding/'+ dst
    # rename() function will
    # rename all the files
    os.rename(src, dst)
    a += 1
