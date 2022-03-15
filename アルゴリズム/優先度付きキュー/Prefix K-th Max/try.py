import heapq
N,K = map(int,input().split())
P = list(map(int,input().split()))
F = P[0:K]
heapq.heapify(F)
ans = heapq.heappop(F)
print(ans)
for i in range(K,N):
    if P[i] <= ans:
        print(ans)
    else:
        heapq.heappush(F,P[i])
        ans = heapq.heappop(F)
        print(ans)

