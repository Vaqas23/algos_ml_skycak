class EulerEstimator:

    def __init__(self, derivatives):
        self.derivatives = derivatives
    
    def estimate_points(self, initial_point, step_size, num_steps):

        arr = [initial_point]

        for i in range(num_steps):
            
            # x

            x_next = arr[i][0] + step_size

            # ys

            next_dict = {}

            current_t, current_state = arr[i]

            for var, func in self.derivatives.items():
                next_dict[var] = current_state[var] + step_size * func(current_t, current_state)
    

            arr.append((x_next, next_dict))

        return arr

    def eval_derivative_at_point(self, initial_point):
        
        t, state = initial_point
        
        dictionary = {}

        for var, func in self.derivatives.items():
            dictionary[var]= func(t, state)

        return dictionary


# Example

def da_dt(t, state):
    return state['a'] + 1

def db_dt(t, state):
    return state['a'] + state['b']

def dc_dt(t, state):
    return 2 * state['b'] + 3 * t

derivatives = {'a': da_dt, 'b': db_dt, 'c': dc_dt}
euler = EulerEstimator(derivatives)

initial_state = {'a': -0.45, 'b': -0.05, 'c': 0}
initial_point = (-0.4, initial_state)

print(euler.estimate_points(initial_point, step_size=2, num_steps=3))