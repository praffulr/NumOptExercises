import casadi as ca

# create empty optimization problem
opti = ca.Opti()

# define variables
x = opti.variable()
y = opti.variable()

# define objective
f = x**2 - 2 * x + y**2 + y

# hand objective to casadi, no minimization done yet
opti.minimize(f)  # opti.minimize(x**2 - 2*x) would also work

# define constraints. To include several constraints, just call this
# function several times
opti.subject_to(x >= 1.5)
opti.subject_to(x + y >= 0)
# opti.subject_to( x  <= 8  )

# define solver
opti.solver("ipopt")  # Use IPOPT as solver
# opti.solver('sqpmethod')              # Use sqpmethod as solver

# solve optimization problem
sol = opti.solve()

# read and print solution
xopt = sol.value(x)
yopt = sol.value(y)

print()
if opti.stats()["return_status"] == "Solve_Succeeded":  # if casadi returns successfully
    print(f"Optimal solution found: x = {xopt}, y = {yopt}")
else:
    print("Problem failed")
