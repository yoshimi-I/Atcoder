
N,M = map(int,input().split())
path = []
for i in range(M):
    a,b,c = map(int,input().split())
    path.append([a,b,c])
point = [-(10**20)]*(N+1)
point[1] = 0
check_ans = 0
for i in range(N):
    for a,b,c in path:
        if point[b] < point[a] + c:
            point[b] = point[a] + c
    if i == N-2:
        check_ans = point[N]

if check_ans != point[N]:
    print("inf") 
else:
    print(point[N])
