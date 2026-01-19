# Creates a list lists
w, h = 4, 3
Matrix = [[0 for x in range(w)] for y in range(h)]
# Matrix[y index][x index]
Matrix[0] = [2,1,1,5]
Matrix[1] = [4,-6,0,-2]
Matrix[2] = [-2,7,2,9]

print(Matrix)

'''a=Matrix[1][0]/Matrix[0][0]
Matrix[1][0]=Matrix[1][0]-a*Matrix[0][0]
Matrix[1][1]=Matrix[1][1]-a*Matrix[0][1]
Matrix[1][2]=Matrix[1][2]-a*Matrix[0][2]'''

'''for i in range(1,h):
    a = Matrix[i][0]/Matrix[0][0]
    for j in range(0,w):
        Matrix[i][j]=Matrix[i][j]-a*Matrix[0][j]

for i in range(2,h):
    a = Matrix[i][1]/Matrix[1][1]
    for j in range(1,w):
        Matrix[i][j]=Matrix[i][j]-a*Matrix[1][j]'''

for i in range(0,w-1):
    for j in range(1+i,h):
        a = Matrix[j][i]/Matrix[i][i]
        for k in range(i,w):
            Matrix[j][k]=Matrix[j][k]-a*Matrix[i][k]



print(Matrix)