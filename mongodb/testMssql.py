#! python 3

import pymssql

'''
conn = pymssql.connect('192.168.0.2', 'sa', 'Welcome1!', 'ygc_suppliers')

cursor = conn.cursor(as_dict=True)

cursor.execute('select top 5 * from dbo.allinfo')
row = cursor.fetchone()
while row:
    print(row['cs'])
#    print(row[3])
#    print(row,)
    row = cursor.fetchone()

conn.close()
'''

i = 1
c = 1
an = 0
arr = []
total = 3000

with pymssql.connect('192.168.0.2', 'sa', 'Welcome1!', 'ygc_suppliers') as conn2:
    with conn2.cursor(as_dict=True) as cur:
        while (i < total):
            print('cycle: ' + str(c))
            cur.execute('select top 1000 * from dbo.allinfo where id > ' + str(i-1) + ' order by id asc')
            '''
            for r in cur:
                _id = r['id']
                cs = r['cs']
                gsmz = r['gsmz']
                xm = r['xm']
                dh = r['dh']
                sj = r['sj']
                cz = r['cz']
                dz = r['dz']
                zycp = r['zycp']
                zyhy = r['zyhy']
                nyye = r['nyye']
                qylx = r['qylx']
                jyms = r['jyms']
                zczb = r['zczb']
                gsjj = r['gsjj']
                doc = {'id': _id, 
                'cs':cs, 'gsmz': gsmz,
                'xm':xm,'dh':dh,
                'sj':sj,'cz':cz,
                'dz':dz,'zycp':zycp,
                'zyhy':zyhy, 'nyye':nyye,
                'qylx':qylx, 'jyms':jyms,
                'zczb':zczb, 'gsjj':gsjj}
                print(doc)
                #print(r['gsmz'])
                i = i+1
            '''
            for r in cur:
                '''                
                if ((i % 1000) == 1):
                    print(i)
                
                if ((i % 1000) == 999):
                    print(i)
                '''
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
                    # insert , the next Id = i + 1
                    print(len(arr))
                    print('insert')

                    # empty the variable
                    del arr[:]
                    print(len(arr))
                    an = 0
                
                i = i + 1
            
            c = c + 1

print ('done')