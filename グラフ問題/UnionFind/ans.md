# UnionFind 
## 問題
- [Union Find](https://atcoder.jp/contests/atc001/tasks/unionfind_a)
## 解答
```
N,Q = map(int,input().split())
L = list(list(map(int,input().split())) for _ in range(Q))
par = [i for i in range(N+1)]
# 経路圧縮の関数 returnでxの根を返す
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
    if x < y:
        par[y] = par[x]
    elif x >= y:
        par[x] = par[y]

for j in range(Q):
    P = L[j][0]
    A = L[j][1]
    B = L[j][2]
    if P == 0:
        unite(A,B)
    if P == 1:
        same(A,B)
```
## 解説
- まず最初は全ての数が独立しているため、全ての親が各々の数となる。またそれぞれの数の親がわかる配列を用意する。(例えば３の親が1だとする(3の頂点の根が1)とpar[3] = 1となればいい)
- ポイントは関数を３つ用意するということである。
    1. まずは経路圧縮で自分が親であるときは自分の番号を返しそれ以外の時はもう一度findを行うことで親を探すと同時につなぎなおす(def find)
    2. 続いて,お互いの親が同じであるかを確認してprintする関数(def same)
    3. 最後に同じグループに入れることで親を同じにするという関数(def unite)
- 一番難しいと思うのはfind関数である。
    - やりたいことはpar[num]とnumが一致しなかった時つまりnumが根ではない時は一体どこを頂点とした根なのかを知る必要がある。
    - 根であるということはpar[num]とnumが一致しているということなのでpar[num]のnumを見て一致していなかったらpar[par[num]]を見にいく、それも一致していなかったらpar[par[par[num]]]といったようにどんどん進めていき、一致した時の値を入れる。
- 他の関数は比較的簡単だが、unite関数のポイントはx = find(x)で根の値を取得している
またわかりにくいが根であるということよりx = par[x]であるし、y=par[y]であることも自明