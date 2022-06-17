class UniouFind():
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
        if self.rank(x) < self.rank(y):
            #yの方が高さが大きいので、yがxを取り込む形になる
            self.par[x] = self.par[y]
            self.siz[ry] += self.siz[rx]
        else:
            #逆にxの方が高さが大きいので、xがyを取り込む
            self.par[y] = self.par[x]
            self.siz[rx] += self.siz[ry]
            
    def size(self,x):
        # rootで辿っていき、-1をreturnしたときのsizを返却
        return self.siz[self.root(x)]
    