from collections import deque
que = deque()
N,M = map(int,input().split())
path = [[] for _ in range(N)]
for i in range(M):
    A,B = map(int,input().split())
    path[A].append(B)
    path[B].append(A)
check = [0] * (N)
ans = []
que.append(0)
check[0] = 1
print(0)
while len(que) > 0:
    for k in range(len(que)):
        now = que.popleft()
        for i in path[now]:
            if check[i] == 0:
                ans.append(i)
                que.append(i)
                check[i] = 1
    ans.sort()
    print(*ans)
    ans = []