#! python3

import os
import sys

print("start...")

curFolder = sys.path[0]+"/"

tmpFile = "tmp.txt"
targetFile = "ttt1.txt"
targetStr = "(21)"
_num = 23

tmp = open(curFolder + tmpFile, "w+")

if(os.path.exists(curFolder + targetFile)):
    with open(curFolder + targetFile, "r") as f:
        for l in f.readlines():
            if l.strip() != "": 
                tmp.write(l.replace(targetStr, "("+str(_num)+")"))
                _num = _num + 1
            else:
                tmp.write(" ")
else:
    print("no such file!")

tmp.close()


print("done...")