def bisection(trials):
    upperbound = 3
    lowerbound = 1
    guess = 0  # This is the also the midpoint
    for i in range(trials):
        guess = (upperbound + lowerbound)/2
        output = (guess)**3 - 2
        if output > 0:
            upperbound = guess
        elif output < 0:
            lowerbound = guess
        else:
            return guess
    return guess


print(bisection(1000))

# Given how python does floats (64 bits, 15-17 significant decimals), you answer won't change after ~100, whether its 100 vs 1,000,000.
# Ex. bisection(1000) == bisection(1000000) evaluates to true.
