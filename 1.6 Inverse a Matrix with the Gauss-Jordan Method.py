# Must be a square matrix
w = h = 4
Matrix = [[0 for x in range(w)] for y in range(h)]
# Matrix[y index][x index]
Matrix[0] = [4,5,7,9]
Matrix[1] = [-1,1,2,-2]
Matrix[2] = [3,-7,7,7]
Matrix[3] = [0,9,8,-1]

print(Matrix)

GJ_Matrix = [[0 for x in range(2*w)] for y in range(h)]

for i in range(w):
    for j in range(h):
        GJ_Matrix[i][j] = Matrix[i][j]

for i in range(w):
    GJ_Matrix[i][w+i] = 1

print(GJ_Matrix)

for i in range(0,w-1):
    for j in range(1+i,h):
        a = GJ_Matrix[j][i]/GJ_Matrix[i][i]
        for k in range(i,2*w):
            GJ_Matrix[j][k]=GJ_Matrix[j][k]-a*GJ_Matrix[i][k]

# This is L^-1
print(GJ_Matrix)

'''a = GJ_Matrix[1][2]/GJ_Matrix[2][2]
for k in range(1,2*w-1):
    GJ_Matrix[1][k]=GJ_Matrix[1][k]-a*GJ_Matrix[2][k]

a = GJ_Matrix[0][2]/GJ_Matrix[2][2]
for k in range(1,2*w-1):
    GJ_Matrix[0][k]=GJ_Matrix[0][k]-a*GJ_Matrix[2][k]

a = GJ_Matrix[0][1]/GJ_Matrix[1][1]
for k in range(1,2*w-1):
    GJ_Matrix[0][k]=GJ_Matrix[0][k]-a*GJ_Matrix[1][k]'''

for i in range(0, w-1):
    for j in range(0, h-1-i):
        a = GJ_Matrix[h-2-i-j][w-1-i] / GJ_Matrix[h-1-i][w-1-i]
        for k in range(1, 2 * w):
            GJ_Matrix[h-2-i-j][k] = GJ_Matrix[h-2-i-j][k] - a * GJ_Matrix[h-1-i][k]

for i in range(0, h):
    a = GJ_Matrix[i][i];
    for j in range(0, 2 * w):
        GJ_Matrix[i][j] = GJ_Matrix[i][j]/a

print(GJ_Matrix)

Inverse_Matrix = [[0 for x in range(w)] for y in range(h)]

for i in range(0, h):
    Inverse_Matrix[i] = GJ_Matrix[i][w:]

print(Inverse_Matrix)