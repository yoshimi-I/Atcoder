N = int(input())
H = list(map(int,input().split()))
H.insert(0,0)
DP = [100000 for _ in range(N+1)]
DP[0] = 0
DP[1] = 0
DP[2] = abs(H[2]-H[1])
for i in range(3,N+1):
    DP[i] = min(DP[i-1]+abs(H[i]-H[i-1]),DP[i-2]+abs(H[i]-H[i-2]))
print(DP[N])
