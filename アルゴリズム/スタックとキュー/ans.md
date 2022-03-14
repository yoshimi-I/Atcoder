# pushpush
## 問題
- [pushpush](https://atcoder.jp/contests/abc066/tasks/arc077_a)
## 解答
```
```
## 解説
- まずは良くない例を以下に示す
```
N = int(input())
A = list(map(int,input().split()))
B = []
def add(a):
    B.append(a)

def sort():
    B.reverse()

for i in range(N):
    add(A[i])
    sort()
print(*B)
```
- このようにやるとRTEが出てしまうことがよくわかると思う。
- 理由は簡単である。reverse()の計算量がO(N)だからである。
- ではどうしたらいいか、とその前に[dequeとqueueとは](deque.md)を読んで欲しい。
- 簡単にまとめると今回はdequeという進化版のキューのライブラリを用いている。
    - このライブラリのメリットは先頭と最後尾をO(N)で取り出したり、追加したりすることができるということである。
- appenleft,popleftのようにleftってつけると順番が逆になる。
- 以下が解答
```
from collections import deque
N = int(input())
A = list(map(int,input().split()))
B = deque()
def add_e(a):
    B.append(a)

def add_f(a):
    B.appendleft(a)

for i in range(N):
    if N % 2 == 0:
        if i % 2 != 0:
            add_f(A[i])
        else:
            add_e(A[i])
    else:
        if i % 2 != 0:
            add_e(A[i])
        else:
            add_f(A[i])
print(*B)
```
- アルゴリズムは簡単であり、Nが偶数なのか、奇数なのかをよく確認する。
そうするとNが偶数の時には木数番目の処理が数字を後ろに付け足すものであり、偶数版目の処理が前に付け足すものであることがわかる。
```
Nが奇数の場合
配列...5 3 1 2 4
順番...⑤③①②④

Nが偶数の場合
配列...4 2 1 3
順番...④②①③
```
- このようにNが奇数の時、下の丸の番号がついた順番だとすると偶数番目の処理は配列の後ろに値を追加、奇数番目の処理は配列の前に値を追加と同じであることがわかる。
- 逆にNが偶数の時、偶数番目の処理は値を配列の先頭に追加、奇数番目の処理は値を配列の末尾に追加と同じであることがわかる。