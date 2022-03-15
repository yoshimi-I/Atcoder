# 順列全探索
## 問題
- [Count Order](https://atcoder.jp/contests/abc150/tasks/abc150_c)
## 解答
```
import itertools
N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))
ls = list(itertools.permutations(range(1,N+1)))
print(abs(ls.index(P)-ls.index(Q)))
```
## 解説
- ポイントとなるところはitertoolsを用いたことによる順列の全探索
    - 詳しくは[itertools](itertools.md)を確認してほしい
- また今回はlistではなくtuple(普通のカッコの中に文字列を格納するやつ)を用いる
    - 理由はls自体は配列だがその中に含まれる形がtupleだからである
```
print(ls)
>>> [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```
- 以上のようにタプルの形で格納されているため、ls.index(同じ値が格納されている番号を返す)ときに、型が同じである必要がある
- またitertools.permutationsは後ろにrangeを使うことで作る順列を指定できる。