from numpy import asarray
from numpy.random import rand
from matplotlib import pyplot

# function
def objective(x):
    return x**2

# derivative
def derivative(x):
    return 2*x

# gradient descent
def gradient_descent(n_iter, step_size):

    solution = rand(1)

    for i in range(n_iter):

        gradient = derivative(solution)

        solution = solution - step_size * gradient

        score = objective(solution)

        print(i, solution, score)

    return solution

# run algorithm
result = gradient_descent(20, 0.1)

# plot graph
x = asarray([-2,-1,0,1,2])
y = objective(x)

pyplot.plot(x, y)
pyplot.scatter(result, objective(result))
pyplot.show()