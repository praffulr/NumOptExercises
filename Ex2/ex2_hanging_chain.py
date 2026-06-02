import casadi as ca
import matplotlib as mpl
import matplotlib.pyplot as plt


# for people who cannot see the plots
if mpl.get_backend() == "agg":
    mpl.use("WebAgg")
print(f"backend: {mpl.get_backend()}")


# create empty optimization problem
opti = ca.Opti()

N = 40

# TODO: complete the definition of variables HERE
# HINT: opti.variable(n) creates a column vector of size n
#       opti.variable(n,m) creates a n-by-m matrix
#       so opti.variable(n,1) is the same as opti.variable(n)
y = opti.variable(N)
z = opti.variable(N)

m = 4 / N  # mass
Di = (70 / 40) * N  # spring constant
g0 = 9.81  # gravity

# defining the objective
Vchain = 0
for i in range(N):
    # TODO: complete the objective function (i.e. potential energy) HERE
    Vchain += m * g0 * z[i]
    if i > 0 and i < N - 1:
        #Ex -1 Q1
        # opti.subject_to(z[i] >= 0.5)
        #Ex -1 Q2
        # opti.subject_to(z[i] - 0.1 * y[i] >= 0.5)
        #Ex - 2 Q1
        # opti.subject_to(z[i] + 0.2 -0.1 * y[i]**2 >= 0)
        #Ex - 2 Q2
        opti.subject_to(z[i] + y[i]**2 >= 0)

    if i != N - 1:
        Vchain += 0.5 * Di * ((y[i + 1] - y[i]) ** 2 + (z[i + 1] - z[i]) ** 2)

# passing the objective to opti
opti.minimize(Vchain)

# TODO: complete the (equality) constraints HERE
opti.subject_to(y[0] == -2)
opti.subject_to(y[-1] == 2)
opti.subject_to(z[0] == 1)
opti.subject_to(z[-1] == 1)

# Setting solver to ipopt and solving the problem:
opti.solver("ipopt")
# opti.solver('sqpmethod')

#Set an initial Guess
opti.set_initial(y, -1)

sol = opti.solve()

# get solution and plot results
Y = sol.value(y)
Z = sol.value(z)

fig, ax = plt.subplots()
ax.plot(Y, Z, "--or")
ax.plot(-2, 1, "xg", markersize=10)
ax.plot(2, 1, "xg", markersize=10)
ax.set_xlabel(r"$y$")
ax.set_ylabel(r"$z$")
ax.set_title(r"Optimal solution hanging chain (without extra constraints)")

## save the plot
plt.savefig("./II.2.2.2.png")

## show plots
plt.show()
