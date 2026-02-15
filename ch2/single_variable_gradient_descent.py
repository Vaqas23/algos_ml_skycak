def minimize_first_equation(guess, tolerance):  # for f(x) = x**2 + x + 1
    learning_rate = 0.01

    while True:
        fx_prime = 2 * guess + 1
        new_guess = guess - learning_rate * fx_prime
        if abs(fx_prime) < tolerance:
            break
        guess = new_guess

    return new_guess


# print(minimize_first_equation(-2, 1e-8))
# print(minimize_first_equation(0, 1e-8))
# print(minimize_first_equation(2, 1e-8))


# for f(x) = x**3 - x**4 - x**2, points down
def maximize_second_equation(guess, tolerance):
    learning_rate = 0.01
    while True:
        fx_prime = (3*guess**2) - (4*guess**3) - (2*guess)
        new_guess = guess + learning_rate * fx_prime  # + because we are finding maximum
        if abs(fx_prime) < tolerance:
            break
        guess = new_guess

    return new_guess


# print(maximize_second_equation(-5, 1e-10))
# print(maximize_second_equation(0, 1e-10))
# print(maximize_second_equation(5, 1e-10))
