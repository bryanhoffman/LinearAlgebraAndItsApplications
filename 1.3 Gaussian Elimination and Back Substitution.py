# Creates a list lists
w, h = 5, 4
Matrix = [[0 for x in range(w)] for y in range(h)]
# Matrix[y index][x index]
Matrix[0] = [1,2,3,4,5]
Matrix[1] = [2,3,5,7,11]
Matrix[2] = [1,3,5,7,9]
Matrix[3] = [1,4,9,16,25]

for i in range(0,w-1):
    for j in range(1+i,h):
        a = Matrix[j][i]/Matrix[i][i]
        for k in range(i,w):
            Matrix[j][k]=Matrix[j][k]-a*Matrix[i][k]

print(Matrix)

solution = [0]*h

'''solution[h-1] = Matrix[h-1][w-1]/Matrix[h-1][w-2]

solution[h-2] = (Matrix[h-2][w-1]-Matrix[h-2][w-2]*solution[h-1])/Matrix[h-2][w-3]
print(solution)'''

for i in range(0,h):
    sum=0.0
    for j in range(0,h):
        sum=sum+Matrix[h-1-i][w-2-j]*solution[h-1-j]

    solution[h-1-i]=(Matrix[h-1-i][w-1]-sum)/Matrix[h-1-i][w-2-i]

print(solution)