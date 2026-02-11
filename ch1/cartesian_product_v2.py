def calc_cartesian_product(ranges):
    points = [
        []
    ]
    for range in ranges:
        new_points = []
        for point in points:
            for single_point in range:
                # using just point would change the original point variable.
                new_point = list(point)
                new_point.append(single_point)
                new_points.append(new_point)
        points = new_points

    return points
