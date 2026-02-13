def newton_raphson(trials):
    guess = 2
    for i in range(trials):
        func_value = (guess)**3 - 2
        tan_fun_value = 3 * ((guess) ** 2)
        root = guess - (func_value/tan_fun_value)
        guess = root
    return guess


print(newton_raphson(2))
