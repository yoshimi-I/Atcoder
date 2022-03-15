# Prefix K-th Max
## 問題
- [Prefix K-th Max](https://atcoder.jp/contests/abc234/tasks/abc234_d)
## 解答
```
import heapq
N,K = map(int,input().split())
P = list(map(int,input().split()))
F = P[0:K]
heapq.heapify(F)
ans = heapq.heappop(F)
print(ans)
for i in range(K,N):
    if P[i] <= ans:
        print(ans)
    else:
        heapq.heappush(F,P[i])
        ans = heapq.heappop(F)
        print(ans)
```
## 解説
- 最小値が変わっていくタイプの問題は間違いなく優先度付きキューを用いる。
- アルゴリズムは最初に配列を用意し、その中での最小値を求める。(最初はそれが解になる)
    - この時、最小値は配列の外に出しておく。
- その後、新しく入ってくる値と最小値を見比べて、最小値より小さかったら解はそのまま
- 最小値より大きかった場合は最小値となる値を配列から取り除き、解を更新する。