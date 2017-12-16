
import os

def SearchPath(path, txt):
    itemlist = os.listdir(path)
    for f in itemlist:
        fullpath = path + "/" + f
        if(os.path.isfile(fullpath)):
            Record(fullpath, txt)
        if(os.path.isdir(fullpath)):
            SearchPath(fullpath, txt)

def Record(msg, path):
    with open(path,'a', encoding='utf8') as fr:
        fr.write(msg)
        fr.write('\n')

def main(path):
    #cur = os.getcwd() + "/LPractice"
    _txt = path + "/resutl.txt"
    if(os.path.isfile(_txt)):
        os.remove(_txt)
    
    SearchPath(path, _txt)
    print("done")

#main()
