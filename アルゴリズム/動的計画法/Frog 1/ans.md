#  Frog 1
## 問題
- [Frog 1](https://atcoder.jp/contests/dp/tasks/dp_a)
## 解答
```
N = int(input())
h = list(map(int,input().split()))
table = [0]*N
a = 0
b = 0
for i in range(1,N):
    if i == 1:
        table[1] = abs(h[1]-h[0])
    else:
        a = table[i-1] + abs(h[i] -h[i-1])
        b = table[i-2] + abs(h[i] -h[i-2])
        table[i] = min(a,b)
print(table[N-1])
```
## 解説
- 動的計画法は3つのプロセスに基づいて行われている。
    - 問題をいくつかの簡単で小さな問題に分割
    - それぞれの問題の計算結果を表に記録
    - 同じ問題に対しては表から計算結果を参照する
1. そのためまずはどういった経緯になるのかを表などを作ることで表示する。
2. そしてn-1から飛んだ方が値が小さくなるのか,n-2から飛んだ方が値が小さくなるのかを見極めて小さい方の値をそれぞれ配列に代入していく。
3. 最終的に配列の最後の値が問題の答えとなるのでその値を出力すればいい