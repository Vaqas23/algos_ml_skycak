import random
import time


def random_draw(distribution):
    start_time = time.time()  # begin count
    trials = 1000000
    cumulative_distribution = distribution
    return_list = [0.0] * len(distribution)
    for i in range(1, len(distribution)):
        # cumulative distribution does work. Gets weird floating point numbers sometimes
        cumulative_distribution[i] += cumulative_distribution[i-1]
    for j in range(trials):  # do set number of trials.
        chance = random.random()
        # increases count by 1 everytime an index is matched to the probability
        for k in range(len(cumulative_distribution)):
            if chance < cumulative_distribution[k]:
                return_list[k] += 1
                break
    # divide all indexes by number of trials to get probability
    for i in range(len(return_list)):
        return_list[i] = return_list[i] / trials

    # time taken
    computation_time = time.time() - start_time
    print(f"Computation time: {round(computation_time, ndigits=3)} seconds")

    return return_list


print(random_draw([0.2, 0.2, 0.2, 0.2, 0.2]))
print(random_draw([0.4, 0.4, 0.2]))
print(random_draw([0.5, 0.5]))
