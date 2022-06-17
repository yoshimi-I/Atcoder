# Union-Find
## 解説
- グループ分けを木構造で管理するデータ構造のこと．同じグループに属する＝同じ木に属するという木構造でグループ分けを行う
- 例えば、2つの値が同じグループに属しているかどうかを調べたいと思ったら、その根の値が一致するかどうかを判断すればいい
## ポイント
- ただ根を一緒にするだけだと深さが深くなっていってしまうため。繋ぎ直すたびに全てを根に繋ぎ直すという処理を行う必要がある
- これを経路圧縮という
## 用意する関数
- 今回はclassを用いて実装を行う(使い回しがしたいため)
## 用意するclass変数(初期化)
1. par(x)
    - 要素 x の親頂点の番号 (自身が根の場合は −1)
2. rank(x)
    - 要素 x の属する根付き木の高さ
3. siz(x)
    - 要素 x の属する根付き木に含まれる頂点数

## 用意するメソッド
1. root(x)
    - 根を求める関数
2. issame(x, y)
    - x と y が同じグループに属するか(根が一致するかを求める関数)
3. unite(x, y)
    - x を含むグループと y を含むグループを併合する関数
4. size(x)
    - x を含む根付き木のサイズを求める

## 実装コード
```
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
    
```
## 解説
- ポイントとしてはrootメソッドは他のメソッドを呼ぶときに使うということである。
- また取り込んだ後はrankを増やすことを忘れないようにする必要がある

