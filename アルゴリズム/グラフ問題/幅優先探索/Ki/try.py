from collections import deque
que = deque()
N,Q = map(int,input().split())
path = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    path[a].append(b)
    path[b].append(a)
counter = [0]*(N+1)
for j in range(Q):
    p,x = map(int,input().split())
    counter[p] += x
visited = [0]*(N+1)

que.append(1)
visited[1] = 1
while len(que) > 0:
    now = que.popleft()
    point = counter[now]
    for to in path[now]:
        if visited[to] == 0:
            counter[to] += point
            visited[to] = 1
            que.append(to)
print(*counter[1:])