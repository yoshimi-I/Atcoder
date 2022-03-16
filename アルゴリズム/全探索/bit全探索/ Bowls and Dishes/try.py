N,M = map(int,input().split())
A = list(list(map(int,input().split())) for _ in range(M))
K = int(input())
C = list(list(map(int,input().split())) for _ in range(K))
ans = 0
num = 0
D = [0]*(N+1)

for i in range(2**K):
    for j in range(K):
        if (i >> j) & 1:
            D[C[j][0]] = 1
        else:
            D[C[j][1]] = 1
    for k in range(M):
        if D[A[k][0]] == 1 & D[A[k][1]] ==  1:
            num += 1
    if num >= ans:
        ans = num
    num = 0
    D = [0]*(N+1)
print(ans)


