#! python 3
#   Fred @ 190513
#-*- coding: utf-8 -*-

import sys
import os
import json
import csv

curFolder = sys.path[0]+"\\"
sourcejsonname = curFolder + "carriers.json"
targetcsvname = curFolder + "result.csv"
#print(sourcejsonname)
#print(targetcsvname)

sourcepath = curFolder + sourcejsonname
targetpath = curFolder + targetcsvname

def main():
    print('Start process!')
    try:
        with open(sourcejsonname, "r", encoding='UTF-8') as fs:
            dataobj = json.load(fs)
            #print(type(dataobj))
            #print(dataobj['meta'])
            #print(dataobj['meta']['code'])
            if(dataobj['data']):
                print('start create csv file')
                with open(targetcsvname, "w+", encoding='UTF-8-sig') as ft:
                    #the title line
                    datastr = "名称,编码,中国名称"
                    ft.write(datastr + '\n')
                    for d in dataobj['data']:
                        datastr = ""
                        if('name' in d):
                            datastr += d['name'] + ","
                        if('code' in d):
                            datastr += d['code'] + ","
                        if('name_cn' in d):
                            datastr += d['name_cn'] + ","
                        
                        #print(d['name_cn'])
                        ft.write(datastr + '\n')
            else:
                pass

        print('Process done!')    
    except BaseException as be:
        #print('333') 
        print(be)
        return

main()
#print('111')
