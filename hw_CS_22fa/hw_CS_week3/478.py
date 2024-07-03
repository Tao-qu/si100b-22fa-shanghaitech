a = list(map(int, input().split()))
num = a[len(a)-1]
n , m = num , 1

for i in range(len(a) - 2,-1,-1):
    num = a[i] + 1 / num
    temp = n 
    n = a[i]*n + m
    m = temp
print(n,m)