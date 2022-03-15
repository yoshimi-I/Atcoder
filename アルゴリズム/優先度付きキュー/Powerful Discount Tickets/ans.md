# Powerful Discount Tickets
## 問題
- [Powerful Discount Tickets](https://atcoder.jp/contests/abc141/tasks/abc141_d)
## 解答
```
import heapq
import math
N,M = map(int,input().split())
A = list(map(lambda x: int(x)*(-1), input().split()))
heapq.heapify(A)
for i in range(M):
    a = heapq.heappop(A)
    a = math.ceil(a / 2)
    heapq.heappush(A,a)
print(-1*sum(A))
```
## 解説
- ライブラリについて解説しようと思う
    - heapq
        - 優先度付きキューをインポート(詳しくは[優先度付きキューとは](heapq.md)を見てほしい)
    - math
        - 割り算の計算における切り上げの処理を実行
- アルゴリズム割引券を割引券の回数分最大の値の商品に適応していき、割引券が切れた後の配列内の合計金額を出力するというものである
- つまりやることは
1. 最大値を取り出す
2. 最大値を2で割った商(切り捨て)を配列に挿入
の繰り返しである

- ここで問題となるのが最大値を取り出して、処理を加えて挿入であるが、挿入が例えO(1)だとしても最大値の取得にO(N)かかってしまいRTEとなる。
- そこで優先度付きキューを用いる。
- しかし優先度付きキューも最小値しか取り出せないので、あらかじめ-1をかけた値で入力を受け取る
- mathライブラリをインポートしたのは符号が変わった場合の切り捨ての処理が切り上げの処理になってしまうからである。
