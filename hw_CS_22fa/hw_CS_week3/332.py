in_list = list(map(int, input().split()))
r = in_list[0]
c = in_list[1]

#i确定+-1,确定行或列
#k确定元素
#mn确定坐标
i , k , m , n = 0 , 0 , 0 , 0

#创建一个r*c的矩阵
TTT = [[0 for j in range(c)] for i in range(r)]
T1 = []
# T2 = [1]

if r*c == 0:
    print(T1)
# elif r*c == 1:
#     print(T2)
else:
    #计算循环次数
    if r > c:
        t = 2*c
    else:
        t = 2*r-1
        
    #赋值
    for i in range(0,t):
        if i % 4 == 0:
            for n in range(int(i / 4),c + int(-i / 4)):
                k += 1
                TTT[m][n] = k
                # print(TTT)
        elif i % 4 == 2:
            for n in range(c + int(-i / 4) - 2,int(i / 4) - 1,-1):
                k += 1
                TTT[m][n] = k
                # print(TTT)
        elif i % 4 == 1:
            for m in range(1+int(i / 4),r - int((i + 1) / 4)):
                k += 1
                TTT[m][n] = k
                # print(TTT)
        else:
            for m in range(r - int((i + 1) / 4) - 1 ,int(i / 4),-1):
                k += 1
                TTT[m][n] = k
                # print(TTT)

    print(TTT)