# 解答
```
import heapq
N,K = map(int,input().split())
P = list(map(int,input().split()))
new_list = P[0:K]
list_min = min(new_list)
print(list_min)
heapq.heapify(new_list)
for i in range(K,N):
    if P[i] <= list_min:
        print(list_min)
    else:
        heapq.heappop(new_list)
        heapq.heappush(new_list,P[i])
        list_min = heapq.heappop(new_list)
        print(list_min)
        heapq.heappush(new_list,list_min)
```
# 解説
- 解けなかった(時間切れ)
- 優先度付きキューを用いることで最小値を値を配列を全探索しなくても出力することができるというものである。
- そのため最小値を取り出したり,値を挿入する問題には必ず使うべき解法
- 今回は最初は最小値をprintしてその後に出てくる値と最小値を見比べで大きかったら既存の最小値は配列の外に,
小さかったらその見比べた数字を配列の外へを繰り返していく。

