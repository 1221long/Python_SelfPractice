#!   python 3
#   Fred @ 2017-02-17
#   move all data of table allinfo in MSSql to MongoDB
#   notice: make sure the msdb and mongodb was started and the connection are right

import os
import datetime
import time
import pymssql
from pymongo import MongoClient

# data should be a [] parameter
def mInsert(coll, i_data, u_startid):    
    coll.insert_many(i_data)
    coll.update_one({'flag':'mssqlstartid'}, {'$set':{'value':u_startid} })
    return

# write log
def writeLog(filename,log):
    now = time.strftime("%H:%M:%S")
    with open(filename, "a+") as fp:
        fp.writelines(now + ": " + log)
        fp.write("\n")
    return

# main interface. insertNum: should >= 1000 and times 1000
def main(insertNum):
    today= datetime.datetime.now()
    filename = 'msbulkinsert_' + str(today.year) + str(today.month)+ str(today.day) + '.log'

    mc = MongoClient('localhost', 27017)        # mongodb connection

    db = mc.ygc_suppliers

    coll = db.allinfo

    flagrow = coll.find_one({'flag':'mssqlstartid'})

    #startId = int(flagrow['value'])
    if(not flagrow):
        sId = 1
        coll.insert_one({'flag':'mssqlstartid', 'value':1})
    else:
        sId = int(flagrow['value'])

    print('startId: ' + str(sId))
    #'''
    i = 0 # record increase
    c = 1
    cSpace = '                '
    an = 0
    bulkLastId = ''
    arr = []
    fifteenStars = '***************'

    total = insertNum # 10000  # total records insert. this value should >= 1000 and times 1000

    writeLog(filename, fifteenStars + ' script starts ' + fifteenStars)
    #  ms connection
    with pymssql.connect('192.168.0.2', 'sa', 'Welcome1!', 'ygc_suppliers') as conn2:        
        with conn2.cursor(as_dict=True) as cur:
            while (i < total):
                #print('cycle: ' + str(c))
                writeLog(filename, 'cycle: ' + str(c) + ' start')
                cur.execute('select top 1000 * from dbo.allinfo where id > ' + str(sId + i - 1) + ' and gsmz is not null order by id asc')
                for r in cur:
                    doc = {'id': r['id'], 
                    'cs': r['cs'], 'gsmz': r['gsmz'],
                    'xm': r['xm'],'dh':r['dh'],
                    'sj':r['sj'],'cz':r['cz'],
                    'dz':r['dz'],'zycp':r['zycp'],
                    'zyhy':r['zyhy'], 'nyye':r['nyye'],
                    'qylx':r['qylx'], 'jyms':r['jyms'],
                    'zczb':r['zczb'], 'gsjj':r['gsjj']}
                    arr.append(doc)

                    an = an + 1
                    if((an % 100) == 0):
                        print('start insert...')
                        bulkLastId = r['id']
                        # insert , the next Id = lastestid + 1
                        mInsert(coll, arr, (bulkLastId+1))
                        #print(len(arr))
                        writeLog(filename, cSpace + 'bulkInsert: ' + str(int(i/100) + 1) + ' LastInsertId: ' + str(bulkLastId))
                        
                        # empty the variable
                        del arr[:]
                        an = 0
                        print('end insert......' + str(bulkLastId))
                        
                    i = i + 1
                    
                writeLog(filename, 'cycle: ' + str(c) + ' done')
                c = c + 1

    writeLog(filename, fifteenStars + ' ' + str(total) + ' records done ' + fifteenStars)

    print('script done')
    return

# start scripts

main(1200000)