import math  # required for third equation (includes sin/cos)


def minimize_first_equation(guess, tolerance):  # for f(x) = x**2 + x + 1
    learning_rate = 0.01
    fx_prime = 2 * guess + 1
    new_guess = guess
    while abs(fx_prime) >= tolerance:
        new_guess = guess - learning_rate * fx_prime
        guess = new_guess
        fx_prime = 2 * guess + 1

    return new_guess

# tests
# print(minimize_first_equation(-2, 1e-8))
# print(minimize_first_equation(0, 1e-8))
# print(minimize_first_equation(2, 1e-8))


# for f(x) = x**3 - x**4 - x**2, points down
def maximize_second_equation(guess, tolerance):
    learning_rate = 0.01
    fx_prime = (3*guess**2) - (4*guess**3) - (2*guess)
    new_guess = guess
    while abs(fx_prime) >= tolerance:
        new_guess = guess + learning_rate * fx_prime  # + because we are finding maximum
        guess = new_guess
        fx_prime = (3*guess**2) - (4*guess**3) - (2*guess)

    return new_guess

# tests
# print(maximize_second_equation(-5, 1e-10))
# print(maximize_second_equation(0, 1e-10))
# print(maximize_second_equation(5, 1e-10))


# could do either min or max, since the equation is f(x) = (sin(x))/(1+x**2)
def minimize_third_equation(guess, tolerance):
    learning_rate = 0.1
    fx_prime = ((((math.cos(guess) * (1+guess**2)) -
                (math.sin(guess)*(2 * guess))) / ((1+guess**2)**2)))
    new_guess = guess
    while abs(fx_prime) >= tolerance:
        # just switch from - to + to find the maximum (same abs value anyway)
        new_guess = guess - learning_rate * fx_prime
        guess = new_guess
        fx_prime = ((((math.cos(guess) * (1+guess**2)) -
                    (math.sin(guess)*(2 * guess))) / ((1+guess**2)**2)))
    return new_guess


# tests
# print(minimize_third_equation(0, 1e-8))
# print(minimize_third_equation(0.5, 1e-8))
# print(minimize_third_equation(-0.5, 1e-8))


# for f(x) = 3cos(x) + (x**2 * e**sin(x))
def minimize_fourth_equation(guess, tolerance):
    learning_rate = 0.1
    fx_prime = -3 * math.sin(guess) + 2 * guess * math.e**(math.sin(guess)) + \
        guess ** 2 * math.cos(guess) * math.e**(math.sin(guess))
    new_guess = guess
    while abs(fx_prime) >= tolerance:
        new_guess = guess - learning_rate * fx_prime
        guess = new_guess
        fx_prime = -3 * math.sin(guess) + 2 * guess * math.e**(math.sin(guess)) + \
            guess ** 2 * math.cos(guess) * math.e**(math.sin(guess))

    return new_guess


# tests
# print(minimize_fourth_equation(0.5, 1e-8))
# print(minimize_fourth_equation(0, 1e-8))
# print(minimize_fourth_equation(-0.5, 1e-8))

# ^^ Gives 3 different minimums, the third gives the global minimum.
# Demonstrates importance of multiple guesses!
