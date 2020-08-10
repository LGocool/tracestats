
f = open("trace1_medium.tr", 'r')
rows = f.readlines()

distance = {}  # request tracker

# distance tracker
# map of distances to distance counts
total_distances={}

# count=0
for row in rows:
    row = row.split(" ")
    obj_id = row[1]  # grab the second column, obj_id

    if obj_id not in distance:
        distance[obj_id] = 0

    for key in distance:
        # {"A": 1,
        #  "B": 0}
        if key == obj_id:
            distance[obj_id] += 1
        else:
            distance[key] += 1 
    
    # Record the access count for the current object
    count = distance[obj_id]
    if count not in total_distances: 
        total_distances[count] = 1
    else:
        total_distances[count] += 1

    # Reset the value of the current object
    distance[obj_id] = 0

for key in distance:
    print("key: {}, distance {}".format(key, distance[key]))

