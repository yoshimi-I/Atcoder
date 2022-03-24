N,K = map(int,input().split())
def g_1(num):
    num = str(num)
    A = list(num)
    A.sort(reverse=True)
    B = "".join(A)
    return int(B)
def g_2(num):
    num = str(num)
    A = list(num)
    A.sort()
    B = "".join(A)
    return int(B)
def f(num):
    return g_1(num)-g_2(num)

for i in range(K):
    N = f(N)
print(N)
