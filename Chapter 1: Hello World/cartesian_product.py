
# Loop through each mini array in input
# make a copy of a given mini array

# input in the form of [ [a], [1,2,3]...]
def calc_cartesian_product(ranges):
    # what we will return
    points = [
        []
    ]

    # single range could refer to [a] within [[a],[1,2]]
    for single_range in ranges:
        print(f"Single range = {single_range}")
        # create a copy of points
        points_copy = []
        for item in points:
            points_copy.append(item)
        print(f"points copy  = {points_copy}")
        # points_copy = [ [] ]

        for single_item in single_range:
            print(f"Single item = {single_item}")
            # create points extended
            points_extended = []
            for item in points_copy:
                points_extended.append(item)

            print(f"points copy  = {points_copy}")
            # now make a copy of points, add a single range to it, and add it to points extended.
            for item_index in range(len(points_copy)):
                points_extended[item_index].append(single_item)
            print(f"points extended  = {points_extended}")

            # add points extended to points copied
            for item_index in range(len(points_extended)):
                points_copy[item_index] = points_extended[item_index]
            print(f"points copy  = {points_copy}")

        # copy all the copy points into the original points
        for item_index in range(len(points_copy)):
            points[item_index] = points_copy[item_index]

    return (points)


print(calc_cartesian_product([[1, 2, 3], ['a', 'b']]))
