import random
import time

# Simulates probability of getting heads a certain (num_heads) number of times
#  when you flip a coin num_flips times. Monte Carlo method.

# added computation time


def sim_probability(num_heads, num_flips):
    start_time = time.time()
    num_trials = 10000
    successes_overrall = 0
    for i in range(int(num_trials)):
        successes_per_trial = 0
        for j in range(num_flips):
            chance = random.random()
            if chance < 0.5:
                successes_per_trial += 1
        if successes_per_trial == num_heads:
            successes_overrall += 1
    computation_time = time.time() - start_time

    print(f"Computation time: {round(computation_time, ndigits=3)} seconds")
    return successes_overrall / num_trials


print(sim_probability(1, 2))
