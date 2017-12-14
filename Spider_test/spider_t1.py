#coding=utf-8
import urllib
import urllib2

def getHtml(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    try:
        response = opener.open(url);
    except BaseException, e:
        print e;
        return '';    
    
    # page = urllib.urlopen(url)
    # html = page.read()
    return response

html = getHtml("http://www.thingiverse.com/thing:23")


with open("./record.txt","w+") as f:
    if html != '':
        print >> f, html.read();

    
# print html.geturl()
# print html.info()