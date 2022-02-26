# 区間スケジューリング
## 問題
- [区間スケジューリング](https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_b)
## 解答
```
N = int(input())
L = list(list(map(int,input().split())) for _ in range(N))
L.sort(key=lambda x: x[1]) 
time_start = L[0][0]
time_end = L[0][1] 
ans = 1
for i in range(1,N):
    if L[i][0] >= time_end:
        time_end = L[i][1]
        ans += 1
print(ans)
```
## 解説
- イメージできるかゲーである
- 簡単な話、終了時間が早い順にソートした後、次に受ける仕事が開始できるのか(時間は被っていないか)を見極めていく
- ポイントは終了してから開始するまでに時間が掛かろうが終了時間が同じであればそれは同じ仕事量1であるということなので終了時間が早いものを被らないように選んでいけばいいということである
