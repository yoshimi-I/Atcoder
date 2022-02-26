N = int(input())
L = list(list(map(int,input().split())) for _ in range(N))
L.sort(key=lambda x: x[1]) 
time_start = L[0][0]
time_end = L[0][1] 
ans = 1
for i in range(1,N):
    if L[i][0] >= time_end:
        time_end = L[i][1]
        ans += 1
print(ans)
