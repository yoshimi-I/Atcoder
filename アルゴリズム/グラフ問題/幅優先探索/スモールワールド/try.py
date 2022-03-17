from collections import deque
que = deque()
N,M = map(int,input().split())
path = [[] for _ in range(N)]
for i in range(M):
    A,B = map(int,input().split())
    path[A].append(B)
    path[B].append(A)
check = [0] * N
que.append(0)
check[0] = 1
count = 1
while len(que) > 0:
    if check.count(0) == 0:
        print(max(check))
        exit()
    for j in range(len(que)):
        now = que.popleft()
        for i in path[now]:
            if check[i] == 0:
                check[i] = count
                que.append(i)
    count+=1