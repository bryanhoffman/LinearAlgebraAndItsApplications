from matplotlib.pyplot import hist2d


def echelon_form(Matrix):
    h = len(Matrix)
    w = len(Matrix[0])
    for i in range(0, w - 1):
        for j in range(1 + i, h):
            a = Matrix[j][i] / Matrix[i][i]
            for k in range(i, w):
                Matrix[j][k] = Matrix[j][k] - a * Matrix[i][k]
    return Matrix


def multiply(Matrix1, Matrix2):
    h1 = len(Matrix1)
    w1 = len(Matrix1[0])
    h2 = len(Matrix2)
    w2 = len(Matrix2[0])
    if(h2==w1):
        w, h = w2, h1
        Matrix = [[0 for x in range(w)] for y in range(h)]
        for i in range(0, h1):
            for j in range(0, w2):
                for k in range(0,h2):
                    Matrix[i][j] += Matrix2[k][j] * Matrix1[i][k]
        return Matrix

    else:
        return "Not possible"

def transpose(Matrix):
    h = len(Matrix)
    w = len(Matrix[0])
    Matrix_tau = [[0 for x in range(h)] for y in range(w)]
    for i in range(0, w):
        for j in range(0, h):
            Matrix_tau[i][j] = Matrix[j][i]
    return Matrix_tau

def inverse(Matrix):
    # Must be a square matrix
    h = len(Matrix)
    w = len(Matrix[0])
    if(h==w):

        GJ_Matrix = [[0 for x in range(2 * w)] for y in range(h)]

        for i in range(w):
            for j in range(h):
                GJ_Matrix[i][j] = Matrix[i][j]

        for i in range(w):
            GJ_Matrix[i][w + i] = 1


        for i in range(0, w - 1):
            for j in range(1 + i, h):
                a = GJ_Matrix[j][i] / GJ_Matrix[i][i]
                for k in range(i, 2 * w):
                    GJ_Matrix[j][k] = GJ_Matrix[j][k] - a * GJ_Matrix[i][k]


        for i in range(0, w - 1):
            for j in range(0, h - 1 - i):
                a = GJ_Matrix[h - 2 - i - j][w - 1 - i] / GJ_Matrix[h - 1 - i][w - 1 - i]
                for k in range(1, 2 * w):
                    GJ_Matrix[h - 2 - i - j][k] = GJ_Matrix[h - 2 - i - j][k] - a * GJ_Matrix[h - 1 - i][k]

        for i in range(0, h):
            a = GJ_Matrix[i][i];
            for j in range(0, 2 * w):
                GJ_Matrix[i][j] = GJ_Matrix[i][j] / a


        Inverse_Matrix = [[0 for x in range(w)] for y in range(h)]

        for i in range(0, h):
            Inverse_Matrix[i] = GJ_Matrix[i][w:]

        return Inverse_Matrix