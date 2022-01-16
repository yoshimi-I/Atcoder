# 問題
- [Climbing Takahashi](https://atcoder.jp/contests/abc235/tasks/abc235_b)
## 自分の解答
```
N = int(input())
H = list(map(int,input().split()))
ans = H[0]
for i in range(N-1):
    if H[i+1] > H[i]:
        ans = H[i+1]
    else:
        break
print(ans)
```
## 模範解答
- 同じようなもん
## 反省点
- 特になし