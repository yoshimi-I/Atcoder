from collections import deque
import copy

ans = 0
N,M = map(int,input().split())
P = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,input().split())
    P[A].append(B)
que = deque()
def_counter = [0 for _ in range(N+1)]
counter = copy.copy(def_counter)
for i in range(1,N+1):
    ans += 1
    counter[i] = 1
    que.append(i)
    while len(que) > 0:
        now = que.popleft()
        for j in P[now]:
            if counter[j] == 0:
                que.append(j)
                ans += 1
                counter[j] = 1
    counter = copy.copy(def_counter)
print(ans)



