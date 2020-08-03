"""trace= open(trace_medium,'rt')
requests=0
lines=trace.read()
line=lines.split("\n")
for i in line:
    request+=1
    print (requests)
    trace.close()
"""
trace=open(trace_medium,'r')
lines=trace.realines()
for line in lines:
    columns=line.split(" ")
    unique_OBJ={}
    for i in range(len(columns))
     obj= i[1]
     if obj_id in unique_OBJ:
         unique_OBJ[i]+=1
    elif obj_id not in unique_OBJ:
        unique_OBJ[i]=1
trace.close()
        
