#! pyhon3 
import os
import time

curDir = os.getcwd() + os.sep + "LPractice" + os.sep + "py_files" + os.sep 

print(curDir)

lineCount = 1
cycle = 1
source = curDir + "jgzz.txt"
tagPre = "res"

print("start")

ft = open(curDir + tagPre+"_"+str(cycle)+".txt", "w")

if(os.path.exists(source)):    
    for lineCount, line in enumerate(open(source, 'r')):
        ft.write(line)
        lineCount += 1
        if(lineCount%10000 == 0):
            ft.flush()
            ft.close()
            cycle += 1
            ft = open(curDir + tagPre+"_"+str(cycle)+".txt", "w")
else:
    print("do not find the source file")

ft.flush()
ft.close()

print(lineCount)

print ("Done")