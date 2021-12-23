N = int(input())
t = [list(map(int,input().split())) for i in range(N)]
t.insert(0,[0,0,0])
ans = "Yes"
for i in range(1,N+1):
    time_lag = t[i][0] - t[i-1][0]
    position_lag = abs(t[i][1]-t[i-1][1]) + abs(t[i][2]-t[i-1][2])
    if time_lag < position_lag:
        ans = "No"
        break
    if time_lag%2 != position_lag % 2:
        ans = "No"
        break
print(ans)