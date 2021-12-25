# Minesweeper
## 問題
- [Minesweeper](https://atcoder.jp/contests/abc075/tasks/abc075_b)
## 解答
```
H ,W = map(int,input().split())
S = list(list(input()) for _ in range(H))
for i in range(H):
    S[i].append(".")
    S[i].insert(0,".")
S.insert(0,list("."*(W+2)))
S.append(list("."*(W+2)))

for j in range(1,1+H):
    for k in range(1,W+1):
        if S[j][k] == "#":
            continue
        else:
            check = [S[j-1][k-1],S[j][k-1],S[j+1][k-1],S[j-1][k],S[j+1][k],S[j-1][k+1],S[j][k+1],S[j+1][k+1]]
            S[j][k] = check.count("#")
for a in range(1,1+H):
    for b in range(1,W+1):
        print(S[a][b],end = "")
    print("")
```
## 解説
- 基本的な方針としては配列の全方位(8方向)の文字がどうなっているのかを調べればいい
- ただ問題はこの時一番外側の枠は周りに8方向ないので、全ての配列で同じような処理ができない(エラーになってしまう)
- そのため外枠を覆うようにして外側に"."の配列を追加する。
- そして配列のループを内側(外枠を追加する前の配列)で行うことで実装できた