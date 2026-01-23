from functions import *
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

w, h = 2, 3

A = [[0 for x in range(w)] for y in range(h)]
b = [[0 for x in range(1)] for y in range(h)]

A = [[1,-1],[1,1],[1,2]]
b = [[1],[1],[3]]

A_tau = transpose(A)
Matrix = multiply(A_tau,A)
vals = multiply(A_tau,b)
for i in range(0,w):
    Matrix[i].append(vals[i][0])

soln = solve(Matrix)

print(soln)

x_vals = [0]*h
f = [0]*h

for i in range(0,h):
    x_vals[i] = A[i][1]
    f[i] = b[i][0]

ax.scatter(x_vals, f)
ax.axline((0, soln[0]), slope=soln[1], color='C0', label='least squares approximation')
plt.show()