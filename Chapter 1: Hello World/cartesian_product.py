
# Loop through each mini array in input
# make a copy of a given mini array

def calc_cartesian_product(ranges):
    # what we will return
    points = [
        []
    ]

    # single range could refer to [a] within [[a],[1,2]]
    for single_range in ranges:
        # build a new list of points for this range
        new_points = []
        for point in points:
            for single_item in single_range:
                new_point = list(point)
                new_point.append(single_item)
                new_points.append(new_point)
        points = new_points

    return points


print(calc_cartesian_product([[1, 2, 3], ['a', 'b']]))
