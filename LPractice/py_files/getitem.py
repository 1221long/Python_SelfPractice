
def get(d, v):
    for i in d:
        if(i == v):
            return d[i]
   
d = {1:'a', 2:"b", 3:"c"}

for i in d:
    print(str(i) + ":" + d[i])        

