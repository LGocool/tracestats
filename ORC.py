
#object request counts
"""" make a dictionary as each request as the key and then count how
    many times that one request is requested for example A:5 a is requested a total of 5x's
f= open("trace1_medium.tr", 'r')
rows = f.readlines()
ORC={}
for row in rows:
    row= row.split(" ")
    obj= row[1]
if obj in ORC :
    ORC[obj]+=1
else:
    ORC[obj]=1
RC={}
for key in ORC:
    val= ORC[key]
    if val not in RC:
        RC[val]=1
    else:
        RC[val]+=1
print (RC)
f.close()"""
"""
#Request sizes
f= open("trace1_medium.tr", 'r')
rows = f.readlines()
RS={}

for row in rows:
    row= row.split(" ")
    req=row[2]

if req in RS:
    RS[req]+=1
else:
    RS[req]=1
print(RS)"""

#object sizes

f= open("trace1_medium.tr", 'r')
rows = f.readlines()
OS={}
for row in rows:
    size= row[2]
    val= row[1]

if size not in OS:# adds items including their sizes to the dictionary
    OS[val]=size
    Obj_list=[]
for key in OS:
    if key not in Obj_list:
        Obj_list.append(key)

    Obj_list.sort()
FD={}
for item in Obj_list:
    if item in FD:
        FD[item]+=1
    else:
        FD[item]=1
        print (FD)


""" also object sizes but just reading through the dictionary and 
    making two different dictionaries
f= open("trace1_medium.tr", 'r')
rows = f.readlines()
OS={}
for row in rows:
    obj=row[2]
    obj_id=row[1]
 OS={}
if obj not in OS:
    OS[obj_id]=obj
else:
    OS[obj_id]+=1

OS_FD={}

for key in OS:
    if key not in OS_FD:
        OS_FD[key]=1
    else:
        OS_FD[key]+=1

f.close()"""""












