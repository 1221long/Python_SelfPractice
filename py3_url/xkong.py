#! python 3
#   Fred @ 2017-02-17

import re
import os
import urllib.request
import datetime
import time

startId = 1000
i = 0
pattern_title = re.compile(r'(?<=<div class="x_box"><h1>).+(?=</a></h1>)');

now = datetime.date.today()

while(i<30):
    url = "http://www.xskong.com/" + str(startId+i) + "/";
    
    try:
        req = urllib.request.urlopen(url)
        content = req.read().decode("utf8")
        #print(content)
        s_title = re.search(pattern_title, content)
        if s_title:
                e_title = s_title.group()
                print(str(startId+i))
                print(s_title.group())
                with open("xskongList"+str(now.year)+str(now.month)+ str(now.day) +".txt", "a+") as fp:
                    fp.writelines(str(startId+i) + ": " + s_title.group());
                    fp.write("\n");
        else:
                print("failed");
        i = i + 1
    except BaseException as be:
        print(be)

print('done')
    