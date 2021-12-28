N,W = map(int,input().split())
L = list(list(map(int,input().split())) for _ in range(N))
L.insert(0,[0,0])
DP = list(list([0]*(W+1)) for _ in range(N+1))
for i in range(1,N+1):
    for j in range(1,W+1):
        if L[i][0] <= j:
            DP[i][j] = max(DP[i-1][j],DP[i-1][j-L[i][0]] + L[i][1])
        else:
            DP[i][j] = DP[i-1][j]
print(DP[N][W])