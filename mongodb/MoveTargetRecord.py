#!   python 3
#   Fred @ 2017-02-17
#   move one target row of table allinfo from MSSql to MongoDB
#   notice: make sure the msdb and mongodb was started and the connection are right

import os
import datetime
import time
import pymssql
from pymongo import MongoClient

def main(rowId):
    
    # check whether we alreay moved
    mc = MongoClient('localhost', 27017)        # mongodb connection

    db = mc.ygc_suppliers

    coll = db.allinfo

    flagrow = coll.find_one({'id': rowId})

    if(not flagrow):
        with pymssql.connect('192.168.0.2', 'sa', 'Welcome1!', 'ygc_suppliers') as conn2:
            with conn2.cursor(as_dict=True) as cur:
                cur.execute('select * from dbo.allinfo where id = ' + str(targetRowId))
                for r in cur:
                    doc = {'id':r['id'], 
                    'cs':r['cs'], 'gsmz':r['gsmz'],
                    'xm':r['xm'],'dh':r['dh'],
                    'sj':r['sj'],'cz':r['cz'],
                    'dz':r['dz'],'zycp':r['zycp'],
                    'zyhy':r['zyhy'], 'nyye':r['nyye'],
                    'qylx':r['qylx'], 'jyms':r['jyms'],
                    'zczb':r['zczb'], 'gsjj':r['gsjj']}
                    
                    coll.insert_one(doc)
    else:
        print('we already had this record')
    return

targetRowId = 2001

main(targetRowId)