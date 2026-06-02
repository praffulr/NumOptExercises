import numpy as np
import matplotlib.pyplot as plt

color_centers = "steelblue"
color_r = "darkorange"

# plot helper that plot a single circle
def plot_circle(x, y, r, i):
    # center
    plt.plot(x, y, color=color_centers, marker="x")
    plt.text( x + 0.2, y + 0.2,
            "$(x_" + str(i+1) + ", y_" + str(i+1) + ")$", color=color_centers
    )

    # circle
    theta = np.linspace(0, 2*np.pi, 100)
    plt.plot( x + r * np.sin(theta), y + r * np.cos(theta), color=color_centers)

    # radius line
    angle = -np.pi / 4 - i * np.pi / 6 # radius direction, varying for nice visualization
    plt.plot( [x, x + r * np.cos(angle)], [y, y + r * np.sin(angle)], linestyle="--", color=color_r, linewidth=1.5)
    plt.text(
        x + 0.5 * np.cos(angle + 0.3) * r, y + 0.5 * np.sin(angle + 0.3) * r,
        "$r_" + str(i+1) + "$", color=color_r
    )


# plot helper that plot the solution (square + inscribed circles)
def plot_solution(centers, r, a, filename=None):
    plt.figure(figsize=(6, 6))
    # plot plate boundaries
    plt.plot([0, 0, a, a, 0], [0, a, a, 0, 0], 'k-', linewidth=3)
    # plot circles
    for i in range(len(centers)):
        x, y = centers[i]
        ri = r[i]
        plot_circle(x, y, ri, i)
    # plt.grid(True)
    plt.xlabel('$x$')
    plt.ylabel("$y$")
    plt.axis("equal")
    if filename is not None:
        plt.savefig(filename)
    plt.show()
