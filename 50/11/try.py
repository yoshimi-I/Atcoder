N,K = map(int,input().split())
L = []
for i in range(N):
    A,B = map(int,input().split())
    L.append([A,B])
L.sort()
now = 0
now += K
for i,j in L:
    if i <= now:
        now += j
print(now)
