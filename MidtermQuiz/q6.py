import casadi as ca

opti = ca.Opti()

#Dimension of variable
N = 3

#Variable Definitions
w = opti.variable(N)

#Defining Objective
f = 2*w[0]**2 + w[0]*w[2] + 2*w[2]**2 + 3*w[1] - ca.log(w[2]+1)

opti.minimize(f)

#Constraints
opti.subject_to(w[2] >= 1)
opti.subject_to(w[2] <= 4)
opti.subject_to(-2*w[0]**2 -0.5*w[1]**2 + 3 >= 0)

opti.solver("ipopt")
sol = opti.solve()

print (sol.value(w))


