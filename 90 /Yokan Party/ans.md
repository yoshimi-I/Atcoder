# 001 - Yokan Party
## ソースコード
```
N,L = map(int,input().split())
K = int(input())
A = [0]+ list(map(int,input().split()))
A.append(L)

def ans(x):
    count = 0
    l = 0
    for i in range(N+1):
        l += A[i+1] - A[i]
        if l >= x:
            count += 1
            l = 0
    if count >= K+1:
        return(True)
    else:
        return(False)
left = 0
right = L
while right - left > 1:
    mid = (left + right)//2
    if ans(mid):
        left = mid
    else:
        right = mid
print(left)
```
## 解説
1. X(cm)以上の長さでようかんを切り分けられるかを判定する
2. 1~Lまでで上記1の判定を通るものの最大値を求める
といったようにして解いていく。

```
    if count >= K+1:
```
- なぜK+1なのか
    - 区切りが1だと確かに切り分ける数と辻褄があうが、全てのようかんが与えたれた量以上で切り分けられていないことになる。最後のようかんもある値以上であるためには最後のようかんを切り終わった後にきるというアクションを行う必要があり、その数を含めるとK+1とある。
    - つまり最後の＋１はようかんを切るというよりかは、ある値を超えるためカウント数が増えたための+1である。