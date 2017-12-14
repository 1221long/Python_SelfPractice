#! python2
# author:       Fred @ 2016-10-17
# to do:        get some needed info from thingerverse
#               , save string in excel and the file, image into target folder
# some info:    the start NO. of thingerverse is 20.
import urllib
import urllib2
import datetime
import StringIO
import random
import re
import os
import _mssql
import time
# import xlsxwriter


# main funtion
def main(startId, recordAmount):
    print 'process start';
    # w_log("123", "getImage", "test4");
    if startId == -1:
        e_StartId = g_startId();
    else:
        e_StartId = startId;
    
    _baseUrl = "http://www.thingiverse.com/";     

    if recordAmount <= 0:
        print "please modify the source code to make the parameter(recordAmount) of function Main() which at the end of the source code grate than 0."
    
    pattern_title = re.compile(r'(?<=<meta name="twitter:title" content=").+(?=">)');
    pattern_tags = re.compile(r'(?<=<a href="/tag:).+(?=">)');
    pattern_summary = re.compile(r'(?<=<meta name="twitter:description" content=").+(?=">)');
    pattern_imgs_url = re.compile(r'(?<=<img class="load-delay" data-img=").+(?=" />)');

    while recordAmount > 0:
        e_url = _baseUrl + "thing:" + str(e_StartId);
        print e_url;
        zip_url = e_url + "/zip"; 

        result = g_content(e_url);
        
        # with open("./test.txt", "w+") as t:
        #     print >> t, web_source;

        e_id = 0;
        e_title = "";
        e_summary = "";
        e_zipUrl = "";
        e_tagsStr = "";
        e_imgUrl = "";

        if result['status'] == 'success':
            e_id = e_StartId;
            e_zipUrl = zip_url;

            pagesource = result['content'].read();
            s_title = re.search(pattern_title, pagesource);
            if s_title:
                e_title = s_title.group();
                print s_title.group();
            
            s_tags = re.findall(pattern_tags, pagesource)
            
            _isFirst = True;
            if s_tags:
                for g in s_tags:
                    if(_isFirst):
                        e_tagsStr = e_tagsStr + g;
                        _isFirst = not _isFirst;
                    else:
                        e_tagsStr = e_tagsStr + "," + g;
                    print g;

            s_summary = re.search(pattern_summary, pagesource)

            if s_summary:
                e_summary = s_summary.group();
                print s_summary.group();
            
            with _mssql.connect(server="192.168.0.2", user="sa", password="Welcome1!", database="Thingiverse") as _conn:
                #SP parameter: @thgvs_record bigint, @Title varchar(255), @Summary [nvarchar](4000), @zipURL [nvarchar](2000), @tagsStr [nvarchar](max)
                _conn.execute_query('EXEC dbo.thgvs_insert_info_to_DB %d, %s, %s, %s, %s',(e_id, e_title, e_summary, e_zipUrl, e_tagsStr));

            s_imgs_url = re.findall(pattern_imgs_url, pagesource)

            if s_imgs_url:
                sqlcomm_ins_img = """
                if (select count(1) from dbo.thgvs_img where thgvs_record = %d and URL = %s) = 0
                begin
                    insert into dbo.thgvs_img(thgvs_record, URL) values(%d, %s)
                end
                """

                with _mssql.connect(server="192.168.0.2", user="sa", password="Welcome1!", database="Thingiverse") as _connImg:
                    for g in s_imgs_url:
                        _connImg.execute_non_query(sqlcomm_ins_img, (e_id, g, e_id, g));
                        print g;
        else:
            print "get data failed";

        recordAmount = recordAmount - 1;
        e_StartId = e_StartId + 1;
        time.sleep(0.1);
        if(recordAmount%20 == 0):
            time.sleep(0.3);
        if(recordAmount%100 == 0):
            time.sleep(0.3);
        if(recordAmount%1000 == 0):
            time.sleep(0.5);

    print "process end";

# get content
def g_content(url):
    
    headers = ["Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0"
        , "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36"
        , "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
        , "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"];

    proxies = ["220.189.249.80:80"
        ,"124.248.32.43:80"
        ,"153.34.156.225:8888"
        ,"180.137.164.20:81"
        ,"123.113.13.164:81"
        ,"122.96.59.105:843"];
    
    r_Agent = random.choice(headers);
    r_Proxy = random.choice(proxies);

    req = urllib2.Request(url);
    req.add_header("User-Agent", r_Agent);
    req.add_header("GET", url);

    # proxy_support = urllib2.ProxyHandler({"http":"http://%s" % r_Proxy});
    # opener = urllib2.build_opener(proxy_support);

    # urllib2.install_opener(opener);
    MaxTryNum = 5;
    for tries in range(MaxTryNum):
        try: 
            content = urllib2.urlopen(req);            
            return {'status':'success','content':content};
        except BaseException, e:
            if e == 'HTTP Error 404: Not Found':
                return {'status':'failed','content':'error_404'};                
            if tries < (MaxTryNum - 1) :
                continue;
            else:
                return {'status':'failed','content':'error_try' };        
            

# write log
def w_log(fileSubfix, title, msg):    
    with open("./log_"+ fileSubfix +".log", "a+") as f:
        now = datetime.datetime.now();
        nowStr = now.strftime("%Y-%m-%d %H:%M:%S") + ":" + str(now.microsecond);
        newStr = (nowStr + " " + title + ":" + msg + "\n");
        f.write(newStr);

def g_startId():
    _outId = 0;
    with _mssql.connect(server="192.168.0.2", user="sa", password="Welcome1!", database="Thingiverse") as _conn:
        _conn.execute_query("select max(thgvs_record) as maxId from dbo.thgvs_record");
        for row in _conn:
            _outId = row['maxId'];
    
    if _outId == 0:
        _outId = 20;
    
    return _outId;

# save file to locals, fileType eg: "IMG", "ZIP"
def s_file(url, id, fileType):
    
    IMG_PATH = "./images";
    ZIP_PATH = "./zips";

    if fileType == "IMG":
        localPath = IMG_PATH;
    elif fileType == "ZIP":
        localPath = ZIP_PATH;
    else:
        print "error";

    if os.path.exists(localPath) == False:  
        os.mkdir(localPath);
    if (url.find(".") != -1):
        name = url[url.find('.',len(url) - 5):];
        fileBytes = urllib.urlopen(url);
        f = open(localPath + str(id) + "_" + name, "wb");
        f.write(fileBytes.read());
        f.flush();
        f.close();

# above definition function
# below entry
# if we want to start with the last id in DB, just set start id = -1
main(-1, 1000);