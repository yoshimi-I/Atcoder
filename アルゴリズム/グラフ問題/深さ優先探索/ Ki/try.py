import sys
sys.setrecursionlimit(10**6)
N,Q = map(int,input().split())
P = [[] for _ in range(N+1)]
ans = [[] for _ in range(N+1)]
counter = list([0]*(N+1))
for i in range(N-1):
    a,b = map(int,input().split())
    P[a].append(b)
    P[b].append(a)
for j in range(1,N+1):
    P[j].sort()

for a in range(Q):
    A,B = map(int,input().split())
    counter[A] += B

point_num = 0
def DFS(pre,now,point_num):
    point_num += counter[now]
    ans[now] = point_num
    for k in P[now]:
        if k != pre:
            DFS(now,k,point_num)
DFS(0,1,point_num)
print(*ans[1:])

