import itertools
N,K = map(int,input().split())
L = list(list(map(int,input().split())) for _ in range(N))
test = list(itertools.permutations(range(1,N)))
ans = 0
for i in range(len(test)):
    path = 0
    P = list(test[i])
    first = P[0]
    path += L[0][first]
    if len(P) == 1:
        path = L[0][P[0]] + L[P[0]][0]
    else:
        for j in range(len(P)-1):
            first = P[j]
            end = P[j+1]
            path+=L[first][end]
        path+= L[end][0]
    if path == K:
        ans+=1
print(ans)





