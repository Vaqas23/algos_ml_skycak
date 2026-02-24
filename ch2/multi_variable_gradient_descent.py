import math

# f(x,y) = (x-1)^2 + 3y^2
def minimize_first_equation(guess_x, guess_y, precision):
    learning_rate = 0.01
    fx_prime = 2 * guess_x - 2
    fy_prime = 6 * guess_y
    while abs(fx_prime) >= precision or abs(fy_prime) >= precision:
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


# f(x,y) = y^2 + ycos(x)
def minimize_second_equation(guess_x, guess_y, precision):
    learning_rate = 0.01
    fx_prime = -guess_y * math.sin(guess_x)
    fy_prime = 2 * guess_y + math.cos(guess_x)
    while abs(fx_prime) >= precision or abs(fy_prime) >= precision:
        new_guess_x = guess_x - learning_rate * fx_prime
        new_guess_y = guess_y - learning_rate * fy_prime
        guess_x = new_guess_x
        guess_y = new_guess_y
        fx_prime = -guess_y * math.sin(guess_x)
        fy_prime = 2 * guess_y + math.cos(guess_x)
    guess_x = round(guess_x, 3)
    guess_y = round(guess_y, 3)

    return guess_x, guess_y

# All global minimum given that the function includes a trignometric function, periodic oscillations
# print(minimize_second_equation(-3, -3, 1e-8))
# print(minimize_second_equation(0, 0, 1e-8))
# print(minimize_second_equation(3, 3, 1e-8))

# f(x,y,z) = (x-1)^2 + 3(y-2)^2 + 4(z+1)^2
def minimize_third_equation(guess_x, guess_y, guess_z, precision):
    learning_rate = 0.01
    fx_prime = 2 * (guess_x - 1)
    fy_prime = 6 * (guess_y - 2)
    fz_prime = 8 * (guess_z + 1)
    while abs(fx_prime) >= precision or abs(fy_prime) >= precision or abs(fz_prime) >= precision:
        new_guess_x = guess_x - learning_rate * fx_prime
        new_guess_y = guess_y - learning_rate * fy_prime
        new_guess_z = guess_z - learning_rate * fz_prime
        guess_x = new_guess_x
        guess_y = new_guess_y
        guess_z = new_guess_z
        fx_prime = 2 * (guess_x - 1)
        fy_prime = 6 * (guess_y - 2)
        fz_prime = 8 * (guess_z + 1)
    guess_x = round(guess_x, 3)
    guess_y = round(guess_y, 3)
    guess_z = round(guess_z, 3)

    return guess_x, guess_y, guess_z


# print(minimize_third_equation(2, 2, 2, 1e-8))
# print(minimize_third_equation(0, 0, 0, 1e-8))
# print(minimize_third_equation(-2, -2, -2, 1e-8))

def minimize_fourth_equation(guess_x, guess_y, guess_z, precision):
    learning_rate = 0.01
    fx_prime = 2 * guess_x - (guess_y * guess_z) * \
        math.sin(guess_x * guess_y * guess_z)
    fy_prime = 6 * guess_y - (guess_x * guess_z) * \
        math.sin(guess_x * guess_y * guess_z)
    fz_prime = 8 * guess_z - (guess_x * guess_y) * \
        math.sin(guess_x * guess_y * guess_z)
    while abs(fx_prime) >= precision or abs(fy_prime) >= precision or abs(fz_prime) >= precision:
        new_guess_x = guess_x - learning_rate * fx_prime
        new_guess_y = guess_y - learning_rate * fy_prime
        new_guess_z = guess_z - learning_rate * fz_prime
        guess_x = new_guess_x
        guess_y = new_guess_y
        guess_z = new_guess_z
        fx_prime = 2 * guess_x - (guess_y * guess_z) * \
            math.sin(guess_x * guess_y * guess_z)
        fy_prime = 6 * guess_y - (guess_x * guess_z) * \
            math.sin(guess_x * guess_y * guess_z)
        fz_prime = 8 * guess_z - (guess_x * guess_y) * \
            math.sin(guess_x * guess_y * guess_z)
    guess_x = round(guess_x, 3)
    guess_y = round(guess_y, 3)
    guess_z = round(guess_z, 3)

    return guess_x, guess_y, guess_z


print(minimize_fourth_equation(5, 5, 5, 1e-8))
print(minimize_fourth_equation(0, 0, 0, 1e-8))
print(minimize_fourth_equation(-5, -5, -5, 1e-8))
