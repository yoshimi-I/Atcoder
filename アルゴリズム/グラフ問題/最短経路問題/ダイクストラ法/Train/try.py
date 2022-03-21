from math import ceil
import heapq
N,M,X,Y = map(int,input().split())
root = [[] for _ in range(N+1)]
time = []
come = []
que = []
for i in range(M):
    A,B,T,K = map(int,input().split())
    root[A].append(B)
    root[B].append(A)
    time.append(T)
    come.append(K)
    heapq.heapify(que)
heapq.heappop(que,[X])
while len(que) > 0:
    