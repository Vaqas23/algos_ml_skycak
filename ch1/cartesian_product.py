def calc_cartesian_product(ranges):
    points = [
        []
    ]

    for single_range in ranges:
        new_points = []
        for point in points:
            for single_item in single_range:
                new_point = list(point)
                new_point.append(single_item)
                new_points.append(new_point)
        points = new_points

    return points


print(calc_cartesian_product([[1, 2, 3], ['a', 'b']]))
