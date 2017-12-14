#! python 2
# http://www.xskong.com/1000
# author:       Fred @ 2016-10-26
# purpose:      get the id match the book name 
# http://www.xskong.com/1000/

import re
import os
import urllib2

startId = 1000
i = 0
while i < 5000:

    url = "http://www.xskong.com/" + str(startId+i) + "/";

    req = urllib2.Request(url);
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0");
    req.add_header("GET", url);

    pattern_title = re.compile(r'(?<=<div class="x_box"><h1>).+(?=</a></h1>)');


    try:
        print str(i);
        result = urllib2.urlopen(req, timeout=3); 
        content = result.read();

        # with open("source.txt", "w") as sou:
        #     sou.writelines(content);

        s_title = re.search(pattern_title, content);
        if s_title:
            e_title = s_title.group();
            print str(startId+i);
            print  s_title.group();
            with open("xskongList.txt", "a+") as fp:
                fp.writelines(str(startId+i) + ": " + s_title.group());
                fp.write("\n");
        else:
            print "failed";

    except BaseException, e:
        print e;
    
    i = i + 1;