# Card Game for Two
##　問題
- [Card Game for Two](https://atcoder.jp/contests/abc088/tasks/abc088_b)
## 解答
```
N = int(input())
L = list(map(int,input().split()))
Alice = 0
Bob = 0
list.sort(L, reverse=True)
for i in range(N):
    if i % 2 == 0:
        Alice += L[i]
    else:
        Bob += L[i]
print(Alice-Bob)
```
## 解説
1. まず配列を大きい順に並び替える
    - ソート順の方法は主に2つある(昇順)
        1.  list.sort(配列の名前)
        2. 新しい配列の名前 = sorted(古い配列の名前)
    - 降順も方法は2種類ある
        1. list.sort(配列の名前, reverse=True)
        2. 新しい配列の名前 = sorted(古い配列の名前, reverse=True)
2. 次にアリスとボブがそれぞれ数をとっていくので配列の番号を2で割ってあまりで場合わけ、それを各々に足していき最後に引き算する