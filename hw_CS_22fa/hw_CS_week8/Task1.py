import numpy as np

mat = eval(input())
nmat = np.array(mat)

print(np.rot90(mat, -1).tolist())

def half(x):
    if x % 2 == 0:
        return int(x / 2)
    else:
        return int((x + 1) / 2)
mat_ = (np.array_split(mat,[int(half(len(mat)))],axis=0))[0].tolist()
mat_ = (np.array_split(mat_,[int(half(len(mat_[0])))],axis=1))[0].tolist()
print(mat_)

print(np.flip(mat, axis = 1).tolist())

def invert(x):
    return 255 - x
print(invert(nmat).tolist())