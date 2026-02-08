# For each sequence, write a function to generate an array containing first n terms,
# and then write a separate recursive function to generate the nth term.
# Be sure to work these sequences out by hand and write tests

# Starting with 5, generate each term by multiplying the previous term by 3 and subtracting 4.

# return array of n terms
def one_one(n):
    arr = [5]

    while len(arr) < n:
        previous_term = arr[-1]
        next_term = (previous_term * 3) - 4
        arr.append(next_term)

    return arr


# return nth term
def one_two(n):
    if n == 1:
        return 5
    else:
        previous_term = one_two(n-1)
        return (3 * previous_term) - 4
