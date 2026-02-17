# f(x,y) = (x-1)^2 + 3y^2
def minimize_first_equation(guess_x, guess_y, tolerance):
    learning_rate = 0.01
    fx_prime = 2 * guess_x - 2
    fy_prime = 6 * guess_y
    while abs(fx_prime) >= tolerance or abs(fy_prime) >= tolerance:
        new_guess_x = guess_x - learning_rate * fx_prime
        new_guess_y = guess_y - learning_rate * fy_prime
        guess_x = new_guess_x
        guess_y = new_guess_y
        fx_prime = 2 * guess_x - 2
        fy_prime = 6 * guess_y
    guess_x = round(guess_x, 3)  # just for clarity
    guess_y = round(guess_y, 3)

    return guess_x, guess_y


# print(minimize_first_equation(-3, -0.5, 1e-8))
# print(minimize_first_equation(0, 0, 1e-8))
# print(minimize_first_equation(3, 0.5, 1e-8))
