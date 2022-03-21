N,M = map(int,input().split())
rel = [[] for _ in range(N)]
for _ in range(M):
    F,S = map(int,input().split())
    rel[S].append(F)
