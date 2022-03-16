# Skill Up
## 問題
- [Skill Up](https://atcoder.jp/contests/abc167/submissions/me)
## 解答
```
N,M,X = map(int,input().split())
L = list(list(map(int,input().split())) for _ in range(N))
S = [0]*(M+1)
S[0] = 10000000000
ans = 10000000000
num = 0
for i in range(2**N):
    for j in range(N):
        if (i >> j) & 1:
            for k in range(1,M+1):
                S[k] += L[j][k]
            num += L[j][0]
    if min(S) >= X:
        if num <= ans:
            ans = num
    num = 0
    S = [0]*(M+1)
    S[0] = 10000000000
if ans == 10000000000:
    print(-1)
else:
    print(ans)
```
## 解説
- 方法は同じです。アルゴリズムの経験値を表す配列を用意しbit全探索で処理を繰り返し、配列に経験値を加えていきます。
- ポイントはLの配列の[0]番目は本の値段を表しているため、そのまま配列のSに追加すると配列の数が合わなくなってしまう。
    - またL[0]を数値0にするとmin(S) >= X:の処理で引っかかってしまうので、今回は10000000000という膨大な数をS[0]に代入している。
また全てが満たされなかった時答えが10000000000になってしまうので、その時は-1を出力するようにする。