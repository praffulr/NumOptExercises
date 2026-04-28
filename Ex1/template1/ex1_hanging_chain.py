import casadi as ca
import matplotlib as mpl
import matplotlib.pyplot as plt


# for people who cannot see the plots
if mpl.get_backend() == 'agg':
    mpl.use('WebAgg')
print(f"backend: {mpl.get_backend()}")


# create empty optimization problem
opti = ca.Opti()

N = 40

# TODO: complete the definition of variables HERE
# HINT: opti.variable(n) creates a column vector of size n
#       opti.variable(n,m) creates a n-by-m matrix
#       so opti.variable(n,1) is the same as opti.variable(n)
y = ...
z = ...

m = 4/N           # mass
Di = (70/40)*N    # spring constant
g0 = 9.81         # gravity

# defining the objective
Vchain = 0
for i in range(N):
    # TODO: complete the objective function (i.e. potential energy) HERE
    Vchain += ...

# passing the objective to opti
opti.minimize(Vchain)

# TODO: complete the (equality) constraints HERE
opti.subject_to( ... )

# Setting solver to ipopt and solving the problem:
opti.solver('ipopt')
# opti.solver('sqpmethod')
sol = opti.solve()

# get solution and plot results
Y = sol.value(y)
Z = sol.value(z)

fig, ax = plt.subplots()
ax.plot(Y, Z, '--or')
ax.plot(-2, 1, 'xg', markersize=10)
ax.plot(2, 1, 'xg', markersize=10)
ax.set_xlabel(r'$y$')
ax.set_ylabel(r'$z$')
ax.set_title(r"Optimal solution hanging chain (without extra constraints)")

## show plots
plt.show()
