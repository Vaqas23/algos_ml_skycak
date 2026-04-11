
# Reorganize constraints to have 4 slack variables

arr: list[list[float]] = [
    [20.0,10.0,15.0,0.0,0.0,0.0,0.0,0.0], #maximize
    [3.0,2.0,5.0,1.0,0.0,0.0,0.0,55.0], # constraint
    [2.0,1.0,1.0,0.0,1.0,0.0,0.0,26.0], # constraint
    [1.0,1.0,3.0,0.0,0.0,1.0,0.0,30.0], # constraint
    [5.0,2.0,4.0,0.0,0.0,0.0,1.0,57.0], # constraint
]


basis = [3, 4, 5, 6]

# this is a very similar algorithm to RREF

condition = True
while condition:

    # if there are no positives left in the objective (maximize) function, we are done
    includes_positive = False
    for i in range(len(arr[0])-1):
        if arr[0][i] > 0:
            includes_positive = True
    
    if not includes_positive:
        break

    # step 1, find pivot column (largest positive coefficient in objective row)
    pivot_column = 0
    for i in range(1, len(arr[0]) - 1):
        if arr[0][i] > arr[0][pivot_column]:
            pivot_column = i

    # step 2, find tighest constrain on the pivot column (ratio test)
    # only rows with a positive pivot-column entry are valid
    tighest_constraint = None
    tighest_constraint_row = None
    for i in range(1, len(arr)):
        col_val = arr[i][pivot_column]
        if col_val <= 0:
            continue
        ratio = arr[i][-1] / col_val
        if tighest_constraint is None or ratio < tighest_constraint:
            tighest_constraint = ratio
            tighest_constraint_row = i

    if tighest_constraint_row is None:
        raise ValueError("No valid pivot row found. Problem may be unbounded.")

    # step 3, normalize the tighest_constrain_row by dividing by pivot value
    pivot_val = arr[tighest_constraint_row][pivot_column]
    for i in range(len(arr[tighest_constraint_row])):
        arr[tighest_constraint_row][i] /= pivot_val
    
    # step 4, normalize all other rows to make constraint column 0
    for i in range(len(arr)):
        if i == tighest_constraint_row:
            continue
        ratio = arr[i][pivot_column]
        for j in range(len(arr[i])):
            arr[i][j] -= arr[tighest_constraint_row][j] * ratio

    # step 5: update basis
    basis[tighest_constraint_row - 1] = pivot_column

# read solution
x = [0.0] * (len(arr[0]) - 1)
for i, var in enumerate(basis):
    x[var] = arr[i + 1][-1]

print("x1 =", round(x[0], 2))
print("x2 =", round(x[1], 2))
print("x3 =", round(x[2], 2))
print("Objective =", round(-arr[0][-1], 2))

"""
[0.0, 0.0, 0.0, -1.0, -6.0, 0.0, -1.0, -268.0]
[0.0, 0.0, 1.0, 0.2, -0.8, 0.0, 0.2, 1.6]
[0.0, 1.0, 0.0, 0.6, 2.6, 0.0, -1.4, 20.8]
[0.0, 0.0, 0.0, -0.8, 0.2, 1.0, 0.2, 2.6]
[1.0, 0.0, 0.0, -0.4, -0.4, 0.0, 0.6, 1.8]
Basis: [2, 1, 5, 0]
Solution: [1.8, 20.8, 1.6, 0.0, 0.0, 2.6, 0.0]
Objective: 268.0
"""