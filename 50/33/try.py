class UnionFind():
    def __init__(self,n):
        self.par = [-1]*n
        self.rank = [0]*n
        self.siz = [1]*n
        
    def root(self,x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])#ここには再帰が最後まで終わった時のreturn文が入っている
            return self.par[x]
            # 再帰で繰り返して親にたどりつたらreturn
            
    def issame(self,x,y):
        return self.root(x) == self.root(y)
        # 返り値はboolean型
        
    def unite(self,x,y):
        rx = self.root(x)
        ry = self.root(y)
        if ry == rx:
            return
        if self.rank[rx] < self.rank[ry]:
            #yの方が高さが大きいので、yがxを取り込む形になる(yがxの親)
            self.par[rx] = y
            self.siz[ry] += self.siz[rx]
            self.siz[rx] = self.siz[ry]
            self.rank[ry]+=1
        else:
            #逆にxの方が高さが大きいので、xがyを取り込む(xがyの親)
            self.par[ry] = x
            self.siz[rx] += self.siz[ry]
            self.siz[ry] = self.siz[rx]
            self.rank[rx]+=1
            
    def size(self,x):
        # rootで辿っていき、-1をreturnしたときのsizを返却
        return self.siz[self.root(x)]
    
    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]

N,M = map(int,input().split())
uni = UnionFind(N)
for i in range(M):
    a,b = map(int,input().split())
    uni.unite(a-1,b-1)
ans = 0
for j in range(N):
    if uni.size(j) > ans:
        ans = uni.size(j)
print(ans)


