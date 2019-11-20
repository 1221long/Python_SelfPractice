
#! python3

import os 
import sys

standStr = "public string d1h01 => PspStartDate.HasValue? (PspStartDate.Value > StartDate.AddHours(0) ? \"\" : (PspStartDate.Value < StartDate.AddHours(0) && PspEndDate.Value < StartDate.AddHours(0)? \"\": \"Y\")): \"\";"

tPath = "tmp.txt"

if(os.path.exists(tPath)):
    os.remove(tPath)

fc = open(tPath,"w+")

i = 1
while i <= 168:
    quotient = i / 24
    remainder = i % 24

    if(remainder == 0):
        remainder = 24
        quotient = quotient - 1
    
    newpre = "d"+str(int(quotient)+1) + "h" + str(remainder).zfill(2)

    t = standStr
    t = t.replace("d1h01", newpre).replace("(0)", "("+str(i)+")")
    #print(t)
    #print("")
    fc.write(t)
    fc.write("\n")
    i = i + 1

fc.flush()
fc.close()
print('done')