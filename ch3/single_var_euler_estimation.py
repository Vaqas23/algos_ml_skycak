class EulerEstimator:

    def __init__(self, derivative):
        self.derivative = derivative
        self.points = []
    
    def estimate_points(self, initial_point, step_size, num_steps):

        # x_next = x + step_size
        # y_next = y + step_size * slope_at_current_point

        self.points = [initial_point]

        for i in range(num_steps):
            x_next = self.points[i][0] + step_size
            y_next = self.points[i][1] + step_size * self.derivative(self.points[i][0])
            self.points.append((x_next,y_next))

        return self.points
    
    def eval_derivative(self,initial_point):
        x = initial_point[0]
        return self.derivative(x)
        
def derivative(t):
    return t + 1 

def derivative_2(t):
    return t - 2

# Part 1

euler = EulerEstimator(derivative)
initial_point =(1,4)
euler.eval_derivative(initial_point)
step_size = 0.5
num_steps = 4
plot = euler.estimate_points(initial_point,step_size,num_steps)

# Part 2

euler2 = EulerEstimator(derivative_2)

initial_point1 = (0,-2)
initial_point2 = (0,-1)
initial_point3 = (0,0)
initial_point4 = (0,1)
initial_point5 = (0,2)

num_steps = 10
step_size = 0.5

plot1 = euler2.estimate_points(initial_point1,step_size,num_steps)
plot2 = euler2.estimate_points(initial_point2,step_size,num_steps)
plot3 = euler2.estimate_points(initial_point3,step_size,num_steps)
plot4 = euler2.estimate_points(initial_point4,step_size,num_steps)
plot5 = euler2.estimate_points(initial_point5,step_size,num_steps)