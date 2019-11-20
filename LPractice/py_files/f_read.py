#! python3

import os
import time

print("")

if(os.path.exists("1.txt")):
    with open("1.txt","r+") as f :
        for l in f.readlines():
            print(l)
else:
    print("no that file")

print('done')
