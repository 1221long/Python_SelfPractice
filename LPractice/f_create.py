
#! python3

import os 

tPath = "test.txt"

if(os.path.exists(tPath)):
    os.remove(tPath)

fc = open("test.txt","w")

i = 0
while i < 500000:
    fc.write(str(i+1)+" qweqweqwe")
    fc.write("\n")
    i = i + 1

fc.flush()
fc.close()
print('done')