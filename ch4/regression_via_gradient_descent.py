import math


# We are going to continously look until the derivative (gradRSS) = 0
# or atleast as close as a computer can get to 0

data_1 = [(0.001, 0.01),(2, 4),(3, 9)] # func is y = ax**b

guess_a = 1
guess_b = 1
precision = 1e-8

def gradRSS_one(a,b,data):
    da = 0 
    db = 0
    for (x,y) in data:
        common = 2 * (a*x**b - y) * x ** b
        da += common
        db += common * a * math.log(x)
    return da, db

def grad_descent_func_one(guess_a,guess_b,precision, data):
    learning_rate = 0.001

    gradRSS_a, gradRSS_b = gradRSS_one(guess_a,guess_b,data)# Giving these variables reduces the total number of total calculations required.

    while abs(gradRSS_a) >= precision or abs(gradRSS_b) >= precision: # Could also do something like (new_a - old_a) < precision, this would check that the point is no longer changing meaningfully.
    
        guess_a = guess_a - learning_rate * gradRSS_a
        guess_b = guess_b - learning_rate * gradRSS_b
        gradRSS_a, gradRSS_b  = gradRSS_one(guess_a,guess_b,data)
    
    guess_a = round(guess_a, 3)
    guess_b = round(guess_b, 3)

    return guess_a, guess_b

print(grad_descent_func_one(1,1,precision, data_1))