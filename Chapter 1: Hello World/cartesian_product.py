
# Loop through each mini array in input
# make a copy of a given mini array

# input in the form of [ [a], [1,2,3]...]
def calc_cartesian_product(ranges):
    # what we will return
    points = [
        []
    ]

    # single range could refer to [a] within [[a],[1,2,3]]
    for single_range in ranges:

        # create a copy of points
        points_copy = []
        for item in points:
            points_copy.append(item)

        # copy all the copy points into the original points
        for item_index in range(len(points_copy)):
            points[item_index] = points_copy[item_index]

    return (points)


points = [
    [1]
]

print(points)

points_copy = []
for item in points:
    points_copy.append(item)

print(points_copy)

for item_index in range(len(points_copy)):
    points[item_index] = points_copy[item_index]

print(points)


# print(calc_cartesian_product([[1, 2, 3], ['a', 'b']]))
