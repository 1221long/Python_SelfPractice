#! pyhon3 
import os
import time

print("test 2")
print("")

tPath = "test.txt"

if(os.path.exists(tPath)):
    sTime = time.time()
    print(time.localtime(sTime))
    count = 0
    for count, line in enumerate(open(tPath, 'r')):
        count += 1
    eTime = time.time()
    print(time.localtime(eTime))
    print("")
    useTime = eTime - sTime
    print("%d records used %f time"  %(count,useTime))
else:
    print("no that file")

print('done')