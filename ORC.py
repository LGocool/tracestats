
#object request counts
"""" make a dictionary as each request as the key and then count how
    many times that one request is requested for example A:5 a is requested a total of 5x's"""
f= open("trace1_medium.tr.html", 'r')
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
        RC[val]=0
    else:
        RC[val]+=1

