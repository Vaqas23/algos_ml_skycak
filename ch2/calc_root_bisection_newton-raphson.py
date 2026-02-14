# Instead of # of decimal places I decided to do # of trials. I find it more interesting from a cpu standpoint.

# I am wondering if the way I find upperbound/lowerbound is sufficient
# Currently requires direct calculation of what we are trying to estimate (a**(1/n))

def calc_root_bisection(a, n, trials):
    guess = 0
    lowerbound = (a ** (1/n)) // 1
    upperbound = ((a ** (1/n)) + 1) // 1

    for i in range(trials):
        guess = (upperbound + lowerbound)/2
        output = (guess)**n - a
        if output > 0:
            upperbound = guess
        elif output < 0:
            lowerbound = guess
        else:
            return guess
    return guess


def calc_root_newton_raphson(a, n, trials):
    guess = a
    for i in range(trials):
        func_value = (guess)**n - a
        tan_fun_value = n * ((guess) ** (n-1))
        root = guess - (func_value/tan_fun_value)
        guess = root
    return guess


print(calc_root_bisection(2, 3, 100))
print(calc_root_newton_raphson(2, 3, 1000))
