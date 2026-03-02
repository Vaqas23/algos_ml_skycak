import math

data = [
    [0.14 , 0.14 , 0.28 , 0.44],
    [0.22 , 0.1 , 0.45 , 0.33],
    [0.1 , 0.19 , 0.25 , 0.4 ],
    [0.02 , 0.08 , 0.43 , 0.45],
    [0.16 , 0.08 , 0.35 , 0.3 ],
    [0.14 , 0.17 , 0.31 , 0.38],
    [0.05 , 0.14 , 0.35 , 0.5 ],
    [0.1 , 0.21 , 0.28 , 0.44],
    [0.04 , 0.08 , 0.35 , 0.47],
    [0.11 , 0.13 , 0.28 , 0.45],
    [0.0 , 0.07 , 0.34 , 0.65],
    [0.2 , 0.05 , 0.4 , 0.37],
    [0.12 , 0.15 , 0.33 , 0.45],
    [0.25 , 0.1 , 0.3 , 0.35],
    [0.0 , 0.1 , 0.4 , 0.5 ],
    [0.15 , 0.2 , 0.3 , 0.37],
    [0.0 , 0.13 , 0.4 , 0.49],
    [0.22 , 0.07 , 0.4 , 0.38],
    [0.2 , 0.18 , 0.3 , 0.4 ]
]

# Randomly choose k = 3. This means we guess there are 3 groups in the data.
# We now randomly assign a number 1-3 for each data point. Simply done:

num = 1

numbered_data = []

for datapoint in data:
    
    if num == 4:
        num = 1
    
    point = []
    point.append(num)
    for i in datapoint:
        point.append(i)
    numbered_data.append(point)

    num += 1


# Now organize data into their respective clusters

cluster1 = []
cluster2 = []
cluster3 = []

for datapoint in numbered_data:
    if datapoint[0] == 1:
        cluster1.append(datapoint)
    elif datapoint[0] == 2:
        cluster2.append(datapoint)
    else:
        cluster3.append(datapoint)

# Now calculate centers

cluster1_center = [0.0,0.0,0.0,0.0]
cluster2_center = [0.0,0.0,0.0,0.0]
cluster3_center = [0.0,0.0,0.0,0.0]

# Cluster 1 

for datapoint in cluster1:
    cluster1_center[0] += datapoint[0]
    cluster1_center[1] += datapoint[1]
    cluster1_center[2] += datapoint[2]
    cluster1_center[3] += datapoint[3]

for i in range(4):
    cluster1_center[i] = cluster1_center[i] / len(cluster1)

# Cluster 2

for datapoint in cluster2:
    cluster2_center[0] += datapoint[0]
    cluster2_center[1] += datapoint[1]
    cluster2_center[2] += datapoint[2]
    cluster2_center[3] += datapoint[3]

for i in range(4):
    cluster2_center[i] = cluster2_center[i] / len(cluster2)

# Cluster 3

for datapoint in cluster3:
    cluster3_center[0] += datapoint[0]
    cluster3_center[1] += datapoint[1]
    cluster3_center[2] += datapoint[2]
    cluster3_center[3] += datapoint[3]

for i in range(4):
    cluster3_center[i] = cluster3_center[i] / len(cluster3)

# Round each cluster center to 3 decimal points

cluster1_center = [round(num, 3) for num in cluster1_center]
cluster2_center = [round(num, 3) for num in cluster2_center]
cluster3_center = [round(num, 3) for num in cluster3_center]

for datapoint in numbered_data:
    distance_to_cluster1 = math.sqrt((datapoint[1] - cluster1_center[0])**2 + (datapoint[2] - cluster1_center[1])**2 + (datapoint[3] - cluster1_center[2])**2 + (datapoint[4] - cluster1_center[3])**2)
    distance_to_cluster2 = math.sqrt((datapoint[1] - cluster2_center[0])**2 + (datapoint[2] - cluster2_center[1])**2 + (datapoint[3] - cluster2_center[2])**2 + (datapoint[4] - cluster2_center[3])**2)
    distance_to_cluster3 = math.sqrt((datapoint[1] - cluster3_center[0])**2 + (datapoint[2] - cluster3_center[1])**2 + (datapoint[3] - cluster3_center[2])**2 + (datapoint[4] - cluster3_center[3])**2)
    distance = min(distance_to_cluster1,distance_to_cluster2,distance_to_cluster3)
    if distance == distance_to_cluster1:
        datapoint[0] = 1 # add to cluster 1
    elif distance == distance_to_cluster2:
        datapoint[0] = 2 # add to cluster 2
    else:
        datapoint[0] = 3 # add to cluster 3


# repeat this process until the clusters don't change
