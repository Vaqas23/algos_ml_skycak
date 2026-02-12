def is_hopeless(square):  # must be all ifs so they arent skipped
    if None not in (square[0][0], square[0][1], square[0][2]):
        if square[0][0] + square[0][1] + square[0][2] != 15:
            return True
    if None not in (square[1][0], square[1][1], square[1][2]):
        if square[1][0] + square[1][1] + square[1][2] != 15:
            return True
    if None not in (square[2][0], square[2][1], square[2][2]):
        if square[2][0] + square[2][1] + square[2][2] != 15:
            return True
    if None not in (square[0][0], square[1][0], square[2][0]):
        if square[0][0] + square[1][0] + square[2][0] != 15:
            return True
    if None not in (square[0][1], square[1][1], square[2][1]):
        if square[0][1] + square[1][1] + square[2][1] != 15:
            return True
    if None not in (square[0][2], square[1][2], square[2][2]):
        if square[0][2] + square[1][2] + square[2][2] != 15:
            return True
    if None not in (square[0][0], square[1][1], square[2][2]):
        if square[0][0] + square[1][1] + square[2][2] != 15:
            return True
    if None not in (square[0][2], square[1][1], square[2][0]):
        if square[0][2] + square[1][1] + square[2][0] != 15:
            return True
        return False


def isvalid(square):
    # All rows, columns, and both diagonals must sum to 15
    if square[0][0] + square[0][1] + square[0][2] != 15:
        return False
    elif square[1][0] + square[1][1] + square[1][2] != 15:
        return False
    elif square[2][0] + square[2][1] + square[2][2] != 15:
        return False
    elif square[0][0] + square[1][0] + square[2][0] != 15:
        return False
    elif square[0][1] + square[1][1] + square[2][1] != 15:
        return False
    elif square[0][2] + square[1][2] + square[2][2] != 15:
        return False
    elif square[0][0] + square[1][1] + square[2][2] != 15:
        return False
    elif square[0][2] + square[1][1] + square[2][0] != 15:
        return False
    else:
        return True


def brute_force_magic_squares():
    count = 0
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    square = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

    # following will be the 9 nested for loops
    for num1 in digits:
        square = [
            [num1, None, None],
            [None, None, None],
            [None, None, None]
        ]
        for num2 in digits:
            if num2 in (num1,):
                continue
            else:
                square = [
                    [num1, num2, None],
                    [None, None, None],
                    [None, None, None]
                ]
            for num3 in digits:
                if num3 in (num1, num2):
                    continue
                else:
                    square = [
                        [num1, num2, num3],
                        [None, None, None],
                        [None, None, None]
                    ]
                    if is_hopeless(square):
                        continue
                for num4 in digits:
                    if num4 in (num1, num2, num3):
                        continue
                    else:
                        square = [
                            [num1, num2, num3],
                            [num4, None, None],
                            [None, None, None]
                        ]
                        if is_hopeless(square):
                            continue
                    for num5 in digits:
                        if num5 in (num1, num2, num3, num4):
                            continue
                        else:
                            square = [
                                [num1, num2, num3],
                                [num4, num5, None],
                                [None, None, None]
                            ]
                            if is_hopeless(square):
                                continue
                        for num6 in digits:
                            if num6 in (num1, num2, num3, num4, num5):
                                continue
                            else:
                                square = [
                                    [num1, num2, num3],
                                    [num4, num5, num6],
                                    [None, None, None]
                                ]
                                if is_hopeless(square):
                                    continue
                            for num7 in digits:
                                if num7 in (num1, num2, num3, num4, num5, num6):
                                    continue
                                else:
                                    square = [
                                        [num1, num2, num3],
                                        [num4, num5, num6],
                                        [num7, None, None]
                                    ]
                                    if is_hopeless(square):
                                        continue
                                for num8 in digits:
                                    if num8 in (num1, num2, num3, num4, num5, num6, num7):
                                        continue
                                    else:
                                        square = [
                                            [num1, num2, num3],
                                            [num4, num5, num6],
                                            [num7, num8, None]
                                        ]
                                        if is_hopeless(square):
                                            continue
                                    for num9 in digits:
                                        if num9 in (num1, num2, num3, num4, num5, num6, num7, num8):
                                            continue
                                        else:
                                            square = [
                                                [num1, num2, num3],
                                                [num4, num5, num6],
                                                [num7, num8, num9]
                                            ]
                                        if isvalid(square):
                                            count += 1
                                            print(
                                                f"{square[0]}\n{square[1]}\n{square[2]}\n")
    print(f"Total: {count}")


brute_force_magic_squares()
