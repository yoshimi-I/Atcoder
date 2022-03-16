N,M,X = map(int,input().split())
L = list(list(map(int,input().split())) for _ in range(N))
S = [0]*(M+1)
S[0] = 10000000000
ans = 10000000000
num = 0
for i in range(2**N):
    for j in range(N):
        if (i >> j) & 1:
            for k in range(1,M+1):
                S[k] += L[j][k]
            num += L[j][0]
    if min(S) >= X:
        if num <= ans:
            ans = num
    num = 0
    S = [0]*(M+1)
    S[0] = 10000000000
if ans == 10000000000:
    print(-1)
else:
    print(ans)
