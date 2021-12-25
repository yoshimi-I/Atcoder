# Two Switches
## 問題
- [Two Switches](https://atcoder.jp/contests/abc070/tasks/abc070_b)
## 解答
```
A,B,C,D = map(int,input().split())
ans = 0
if C >= A:
    if D >= B:
        ans = B-C
    else:
        ans = D-C
else:
    if D >= B:
        ans = B-A
    else:
        ans = D-A
if ans < 0:
    ans = 0
print(ans)

```
## 解説
- めっちゃ場合分けしてとく(つまりゴリ押し)
## 別解
```
A,B,C,D = map(int,input().split())
lis=[A,C]
listy=[B,D]
if min(listy)-max(lis) > 0:
  print(min(listy)-max(lis))
else:
  print(0)
```
- 前提条件としてまずボタンを押したタイミングが重なっていたかどうかを場合分けする
- 重なっていなかったら答えは0
- 重なっていた場合、AとCの後に押した方からBとDの先に押した方までの長さを計測するため、max()でA,Cの大きい方をきめ(後に押した方),min()でB,Dの小さい方(先に押した方)を決めて引き算すればいいということである。