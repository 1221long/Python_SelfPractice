#! python 3
#   Fred @ 2019-04-26

import sys
import re
import os

regstr = re.compile(r'(?<=<a href=").+(?=">《绝命毒师》)')

curFolder = sys.path[0]+"\\"
filename = "Untitled-3.txt"
resultfile = "result.txt"
filepath = curFolder + filename
resultpath = curFolder + resultfile
print(filepath)

def PrintAllResultByReg(targetstr,regstr):    
    try:
        results = re.search(regstr, targetstr)
        if results:
            return(results.group())            
    except BaseException as be:
        print(be)

if(os.path.exists(filepath)):
    with open(resultpath, "w+") as fr:
        with open(filepath, "r", encoding='UTF-8') as fp:
            for line in fp.readlines():
                match = PrintAllResultByReg(line,regstr)
                if match:
                    fr.write(match + "\n")
else:
    print('no such file')


