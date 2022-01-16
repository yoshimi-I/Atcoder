# 問題
- [The Kth Time Query](https://atcoder.jp/contests/abc235/tasks/abc235_c)
## 解答
```
from collections import defaultdict
N, Q = map(int, input().split())
A = list(map(int, input().split()))
m = defaultdict(list)
for i in range(N):
  m[A[i]].append(i + 1)
for _ in range(Q):
  x, k = map(int, input().split())
  if k <= len(m[x]):
    print(m[x][k - 1])
  else:
    print(-1)
```
## 解説
- 連想配列を使うことで今回は解くことができる(自分はforのネストしか思いつかなかったためO(N^2)で完全に時間オーバーとなってしまう)
- 今回の肝は
```
from collections import defaultdict
m = defaultdict(list)
for i in range(N):
  m[A[i]].append(i + 1)
```
というdefaultdict()メソッドである,いうならば
- これは通常の辞書のようにキーを指定して値を追加することが可能になるものである
- 使い方は
    1. まずは型の指定(int,dict,list,bool)を行い
        - 今回はlistを用いるためその解説を行う
    2. そこにキーとそれに伴う値を入れていく
- その結果今回は
```
[1 1 2 3 1 2]
```
といいた配列から
```
[1:[1,2,5],2:[3,6],3:[4]]
```
と言いた配列を作成することができる。
- このような配列を作ることで処理を最小化することができる
- 続いて
```
1 1
1 2
1 3
1 4
2 1
2 2
2 3
4 1
```
このような入力を受け取るため,1つ目をキーと照らし合わせ2つ目を値と照らし合わせれば答えを求めることができるということである
- また取り出すときには配列の番号のようにm[n]のnにキーを入れることで出力することができる