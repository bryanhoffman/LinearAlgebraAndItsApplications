from functions import *
#Example from Linear Algebra and its Applications (3rd Edition)
w, h = 3, 3
A = [[1,1,2],[0,0,1],[1,0,0]]

# Example from Wikipedia
# w, h = 2, 2
# A = [[3,2], [1, 2]]
A = transpose(A)

AA_tau = multiply(A,transpose(A))
for i in range(h):
    for j in range(w):
        AA_tau[i].append(A[i][j])

AA_tau = echelon_form(AA_tau)

basis = [[0]*w,[0]*w,[0]*w]

for i in range(h):
    for j in range(w):
        basis[i][j] = AA_tau[i][w+j]

for i in range(h):
    sum = 0
    for j in range(w):
        sum+=basis[i][j]**2
    for j in range(w):
        basis[i][j]/=sum**0.5

message="The basis is formed by the vectors:"
for i in range(w):
    message=message+" "+str(basis[i])

print(message)
