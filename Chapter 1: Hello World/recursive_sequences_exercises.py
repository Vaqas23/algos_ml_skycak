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

# Starting with 25, generate each term by taking half of the
# previous term if it’s even, or multiplying by 3 and adding 1 if
# it’s odd. (This is an instance of a Collatz sequence.)

# return an array of n terms


def two_one(n):
    terms = [25]

    while len(terms) < n:
        previous_term = terms[-1]

        if previous_term % 2 == 0:
            next_term = previous_term // 2
            terms.append(next_term)
        else:
            next_term = (previous_term * 3) + 1
            terms.append(next_term)

    return terms

# return the nth term


def two_two(n):
    if n == 1:
        return 25
    else:
        previous_term = two_two(n-1)
        if previous_term % 2 == 0:
            return previous_term // 2
        else:
            return (previous_term * 3) + 1

# Starting with 0, 1, generate each term by adding the previous
# two terms. (This is the famous Fibonacci sequence.)


def three_one(n):  # give array of n terms
    fibonacci_sequence = [0, 1]
    if n == 1:
        return [0]
    elif n == 2:
        return fibonacci_sequence
    else:
        while len(fibonacci_sequence) < n:
            previous_term1, previous_term2 = fibonacci_sequence[-1], fibonacci_sequence[-2]
            next_term = previous_term1 + previous_term2
            fibonacci_sequence.append(next_term)
    return fibonacci_sequence


# give the nth term. Error was that I was treating it like an array.
def three_two(n):

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        previous_term1 = three_two(n-1)
        previous_term2 = three_two(n-2)
        return previous_term1 + previous_term2

# Starting with 2, −3, generate each term by adding the product
# of the previous two terms.
