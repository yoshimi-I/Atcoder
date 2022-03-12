# Collision 2
## 問題
- [Collision 2](https://atcoder.jp/contests/abc243/tasks/abc243_c)
## 解答
```
N = int(input())
L = list(list(map(int,input().split())) for _ in range(N))
S = list(input())

min = dict()
max = dict()

for i in range(N):
    x = L[i][0]
    y = L[i][1] 

    #方向がR即ち右に進む
    # 最小値の更新を行う
    if S[i] == "R":
        if y in min:
            if min[y] > x:
                min[y] = x
        else:
            min[y] = x

    #方向がL即ち左に進む
    # 最大値の更新を行う
    if S[i] == "L":
        if y in max:
            if max[y] < x:
                max[y] = x
        else:
            max[y] = x
    #yをキーとする値がそれぞれmaxとminに含まれていたとき、minよりmaxの方が大きい場合処理を終了する
    if y in max and y in min:
        if max[y] > min[y]:
            print("Yes")
            exit()

print("No")
```
# 解説
- [連想配列](rensouhairetu.md)をまずは理解しておきたい
- まずこの問題の解法は
    1. 同じyの値を持つものがあるかを確認する
    2. 1を満たすとき、右に進むx座標が最も小さいものAと、左に進むx座標が最も大きいものBを比較した時、Aのx座標 < Bのx座標となっていればいい
- そのためまず最小値と最大値を格納する２つの連想配列(min,max)を用意し、キーをyとする。そして常にmin[y] < max[y]を確認する
- さらに新しい値(さらに大きかったり、小さかったりした値が存在した)時は更新をしていく
- この処理を記載すればいい


