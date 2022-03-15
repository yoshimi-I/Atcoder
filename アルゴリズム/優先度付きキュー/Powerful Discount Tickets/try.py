import heapq
import math
N,M = map(int,input().split())
A = list(map(lambda x: int(x)*(-1), input().split()))
heapq.heapify(A)
for i in range(M):
    a = heapq.heappop(A)
    a = math.ceil(a / 2)
    heapq.heappush(A,a)
print(-1*sum(A))


