class EulerEstimator:

    def __init__(self, derivatives):
        self.derivatives = derivatives
    
    def estimate_points(self, inital_point, step_size, num_steps):
        pass

    def eval_derivative_at_point(self, inital_point):
        pass




def da_dt(t, state):
    return state['a'] + 1

def db_dt(t, state):
    return state['a'] + state['b']

def dc_dt(t, state):
    return 2 * state['b'] + 3 * t
