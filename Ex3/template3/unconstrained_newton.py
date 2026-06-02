"""
    Leo Simpson, University of Freiburg (teacher assistant), 2025.

    This file is for an exercise for the course Numerical Optimization by Prof. Moritz Diehl.
"""

import matplotlib.pyplot as plt
import numpy as np

rho = 10 # set this parameter to 5. You can also play with this parameter.

## Define the objective function
def f(x, y):
    ... # TODO

## Define the gradient:
def gradient(x, y):
   ... # TODO

## Define the Hessian Approximations
def Hessian(x, y, approximation):
    """
        Approximation is a string, equal to one of the following:
         - "exact" for exact Hessian approximation
         - "GN" for Gauss-Newton hessian approximation
         - "steeepest" for alpha I with alpha= 10
    """
    if approximation == "exact":
        return ... # TODO
    elif approximation == "GN":
        return ... # TODO
    elif approximation == "steepest":
        return ... # TODO
    else:
        raise ValueError("Unknown approximation type. Choose from 'exact', 'GN', or 'steepest'.")


def Newton_step(x, y, hessian_approximation):
    """
        Perform a Newton step using the specified approximation for the Hessian.
    """
    grad = gradient(x, y)
    H = Hessian(x, y, hessian_approximation)
    ... # TODO
    return new_x, new_y

def stopping_condition(x, y):
    """
        Check the stopping condition for the Newton method.
    """
    ... # TODO



# Run the algorithm (nothing to do here)
hessian_approximations = ["exact", "GN", "steepest"]
all_iterates = {}
N_max = 50
for hessian_approximation in hessian_approximations:
    iterates = []
    x, y = ... # TODO
    for k in range(N_max):
        iterates.append((x, y))
        x, y = Newton_step(x, y, hessian_approximation)
        if stopping_condition(x, y):
            break
    all_iterates[hessian_approximation] = iterates



# Plot the solutions
plot = "value" # either "3D" or "value"
if plot=="3D":
    N_grid = 500
    X = np.linspace(-10, 10, N_grid)
    Y = np.linspace(-10, 10, N_grid)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(projection='3d', computed_zorder=False)
    ax.grid()
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.set_zlabel(r'$f(x, y)$')


    for hessian_approximation, iterates in all_iterates.items():
        iterates = np.array(iterates)
        x_iterates, y_iterates = iterates[:, 0], iterates[:, 1]
        ax.plot(x_iterates, y_iterates, f(x_iterates, y_iterates), "-o", markersize=3, label=hessian_approximation)
    ax.plot_surface(X, Y, Z)
    ax.legend()
    ax.set_title("Newton's method with different Hessian approximations")
    plt.show()
elif plot=="value":
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlabel(r'number of iterations')
    ax.set_ylabel(r'$f(x_k, y_k)$')
    ax.grid()
    # ax.set_xscale('log')
    ax.set_yscale('log')
    for hessian_approximation, iterates in all_iterates.items():
        f_iterates = ... # TODO
        ax.plot(range(len(f_iterates)), f_iterates, "-o", markersize=3, label=hessian_approximation)
    ax.legend()
    ax.set_title("Newton's method with different Hessian approximations")
    plt.show()