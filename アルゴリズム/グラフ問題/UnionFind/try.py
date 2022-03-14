N,Q = map(int,input().split())
L = list(list(map(int,input().split())) for _ in range(Q))
par = [i for i in range(N+1)]
# 経路圧縮の関数
def find(x):
    if par[x] == x:
        return par[x]
    else:
        par[x] = find(par[x])
        return par[x]

#お互いが同じ親かの判定
def same(x,y):
    if par[x] == par[y]:
        print("Yes")
    else:
        print("No")

# 根を統一
def unite(x,y):
    x = find(x)
    y = find(y)
    if par[x] < par[y]:
        par[y] = par[x]
    elif par[x] >= par[y]:
        par[x] = par[y]

for j in range(Q):
    P = L[j][0]
    A = L[j][1]
    B = L[j][2]
    if P == 0:
        unite(A,B)
    if P == 1:
        same(A,B)






