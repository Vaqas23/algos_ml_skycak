def minimize_first_equation(n, tolerance):
    guess = n
    learning_rate = 0.01

    while True:
        fx_prime = 2 * guess + 1
        new_guess = guess - learning_rate * fx_prime
        if abs(fx_prime) < tolerance:
            break
        guess = new_guess

    return new_guess


print(minimize_first_equation(-2, 1e-8))
print(minimize_first_equation(0, 1e-8))
print(minimize_first_equation(2, 1e-8))
