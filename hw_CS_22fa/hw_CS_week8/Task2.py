import numpy as np

mat = eval(input())
nmat = np.array(mat)


def half(x):
    if x % 2 == 0:
        return int(x / 2)
    else:
        return int((x + 1) / 2)


sam = np.ones([half(len(mat)), half(len(mat[0]))], dtype=int)
for i in range(len(sam)):
    for j in range(len(sam[0])):
        sam[i][j] = mat[2*i][2*j]
print(sam.tolist())

con = np.ones([len(mat)-2, len(mat[0])-2], dtype=int)
for i in range(len(con)):
    for j in range(len(con[0])):
        con[i][j] = int((mat[i][j]+mat[i][j+1]+mat[i][j+2]+mat[i+1][j]+mat[i+1]
                        [j+1]+mat[i+1][j+2]+mat[i+2][j]+mat[i+2][j+1]+mat[i+2][j+2]) / 9)
print(con.tolist())

his = np.ones((16), dtype=int)


def subf(i):
    his_tf = np.logical_and(nmat >= 16*i, nmat < 16*i + 16)
    his[i] = np.sum(his_tf)


subf(0), subf(1), subf(2), subf(3), subf(4), subf(5), subf(6), subf(7)
subf(8), subf(9), subf(10), subf(11), subf(12), subf(13), subf(14), subf(15)
print(his.tolist())
