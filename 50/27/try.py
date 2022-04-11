from collections import deque


N,M = map(int,input().split())
P = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,input().split())
    P[A].append(B)
que = deque()



